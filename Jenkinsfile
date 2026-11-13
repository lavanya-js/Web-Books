
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                echo 'Checking Python installation'
                bat 'python --version'
                bat 'where python'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated tests'
                bat 'python -m unittest app'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running Python application'
                bat 'python app.py'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }

        failure {
            echo 'CI pipeline failed'
        }
    }
}
