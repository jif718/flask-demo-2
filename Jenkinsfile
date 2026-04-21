pipeline {
    agent none

    environment {
        IMAGE = 'linux02.local/flask-demo/flask-demo'
        TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Python CI Check') {
            agent {
                label 'python'
            }

            stages {
                stage('Check Python') {
                    steps {
                        sh 'python3 --version'
                        sh 'pip3 --version'
                    }
                }

                stage('Create Virtualenv') {
                    steps {
                        sh 'python3 -m venv .venv'
                    }
                }

                stage('Install Dependencies') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }

                stage('Syntax Check') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            python -m py_compile app.py
                        '''
                    }
                }

                stage('Import Flask App') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            python -c "import app; print('Flask app import success')"
                        '''
                    }
                }

                stage('Run Flask App and Health Check') {
                    steps {
                        sh '''
                            . .venv/bin/activate

                            nohup python app.py > flask.log 2>&1 &
                            echo $! > flask.pid

                            sleep 5

                            echo "=== flask.log ==="
                            cat flask.log || true

                            echo "=== curl check ==="
                            curl -s http://127.0.0.1:8080/ | tee curl.out

                            grep -q "Hello from Flask Demo" curl.out
                        '''
                    }
                }
            }

            post {
                always {
                    sh '''
                        if [ -f flask.pid ]; then
                            kill $(cat flask.pid) || true
                        fi
                    '''
                }
            }
        }

        stage('Build and Push Image') {
            agent {
                label 'kaniko'
            }

            steps {
                container('kaniko') {
                    sh '''
                        /kaniko/executor \
                          --context "${WORKSPACE}" \
                          --dockerfile "${WORKSPACE}/Dockerfile" \
                          --destination "${IMAGE}:${TAG}" \
                          --registry-certificate=linux02.local=/kaniko/certs/ca.crt
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "镜像已成功推送到 Harbor: ${IMAGE}:${TAG}"
            echo "后续请手动使用 Helm 部署这个镜像"
        }
        failure {
            echo '流水线失败，请查看日志排查'
        }
    }
}
