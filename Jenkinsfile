pipeline {
    agent any

    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sakshichavhan-bit/python-flask-project.git'
                
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t python-app .
                sh "docker tag python-app:$IMAGE_TAG sakshi44/python-flask-app"
                
            }
        }

        stage('Push to Docker Hub') {
            steps {
                 sh "docker push sakshi44/python-flask-app"               
           }
       }
        stage('Deploy to container'){
            steps{
                sh 'docker run -d -p 8080:5000 sakshi44/python-flask-app'
            }
        }
        
}
