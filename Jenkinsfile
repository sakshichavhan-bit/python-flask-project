pipeline {
    agent any

    environment {
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sakshichavhan-bit/python-flask-project.git'
                
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t python-app:$IMAGE_TAG .
                sh "docker tag python-app:$IMAGE_TAG sakshi44/python-flask-app:$IMAGE_TAG"
                
            }
        }

        stage('Push to Docker Hub') {
            steps {
                 sh "docker push sakshi44/python-flask-app:$IMAGE_TAG"               
           }
       }
        stage('Deploy to container'){
            steps{
                sh 'docker run -d -p 8080:80 sakshi44/python-flask-app:$IMAGE_TAG'
            }
        }
        

    post {
        success {
            echo 'Docker image pushed successfully to Docker Hub.'
        }
        failure {
            echo 'Pipeline failed. Check Jenkins console logs.'
        }
        always {
            sh 'docker image prune -f || true'
        }
    }
}
