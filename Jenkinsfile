pipeline {
    agent any

    environment {
        HARBOR_USER = 'admin'
        HARBOR_PASS = credentials('harbor-credentials')
        IMAGE = "linux02.local/flask-demo/flask-demo"
        TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "代码已检出：${GIT_COMMIT}"
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE}:${TAG} ."
            }
        }

        stage('Push to Harbor') {
            steps {
                sh """
                    echo ${HARBOR_PASS} | docker login linux02.local -u ${HARBOR_USER} --password-stdin
                    docker push ${IMAGE}:${TAG}
                    docker logout linux02.local
                """
            }
        }

        stage('Deploy to K8s') {
            steps {
                sh """
                    sed -i 's|IMAGE_PLACEHOLDER|${IMAGE}:${TAG}|g' k8s/deployment.yaml
                    kubectl apply -f k8s/
                    kubectl rollout status deployment/flask-demo --timeout=60s
                """
            }
        }
    }

    post {
        success { echo "部署成功：${IMAGE}:${TAG}" }
        failure {
            sh "kubectl describe pods -l app=flask-demo || true"
            sh "kubectl logs -l app=flask-demo --previous || true"
        }
        always {
            sh "docker rmi ${IMAGE}:${TAG} || true"
        }
    }
}
