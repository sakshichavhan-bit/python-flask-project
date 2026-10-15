pipeline {
    agent any

    environment {
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r app/requirements.txt
                    python3 -c "from app.app import app; \
                    assert app.test_client().get('/health').status_code == 200"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t python-app:$IMAGE_TAG .
                sh "docker tag python-app:$IMAGE_TAG sakshi44:$IMAGE_TAG"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                 sh "docker push sakshi44:$IMAGE_TAG"               
        }
    }

    post {
        success {
            echo 'Docker image pushed successfully to ECR.'
        }
        failure {
            echo 'Pipeline failed. Check Jenkins console logs.'
        }
        always {
            sh 'docker image prune -f || true'
        }
    }
}
