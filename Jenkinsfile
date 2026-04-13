pipeline {
    agent any

    environment {
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
                withCredentials([usernamePassword(
                    credentialsId: 'harbor-credentials',
                    usernameVariable: 'HARBOR_USER',
                    passwordVariable: 'HARBOR_PASS'
                )]) {
                    sh 'echo $HARBOR_PASS | docker login linux02.local -u $HARBOR_USER --password-stdin'
                    sh 'docker push $IMAGE:$TAG'
                    sh 'docker logout linux02.local'
                }
            }
        }
    }

    post {
        success { echo "镜像已推送：${IMAGE}:${TAG}" }
        failure { echo "构建失败，查看日志" }
        always  { sh 'docker rmi $IMAGE:$TAG || true' }
    }
}
