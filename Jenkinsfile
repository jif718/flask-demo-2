pipeline {
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
    }

    post {
        success {
            echo 'Python CI 检查通过'
        }
        failure {
            echo 'Python CI 检查失败，请查看日志'
        }
    }
}
