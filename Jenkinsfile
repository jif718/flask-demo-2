pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    credentialsId: 'gitea-credentials',
                    url: 'http://linux03.local:3000/admin/flask-demo.git'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Import Flask App') {
            steps {
                sh 'python3 -c "import app; print(\'Flask app import success\')"'
            }
        }
    }
}
