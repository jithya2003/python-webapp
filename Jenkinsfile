pipeline{
    agent any
    environment{
        IMAGE_NAME="python-webapp"
        SONARQUBE="SonarQube"
    }
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main', url:'https://github.com/jithya2003/python-webapp.git'
            }
        }
        stage('Build Docker Image'){
            steps{
                script{
                    docker.build("${IMAGE_NAME}:latest")
                }
            }
        }
        stage('Scan with Trivy'){
            steps{
                sh "trivy image --severity HIGH,CRITICAL --exit-code 1 python-webapp:latest"
            }
        }
        stage('Scan with SonarQube'){
            environment{
                scannerHome = tool 'SonarScanner'
            }
            steps{
                withSonarQubeEnv("${SONARQUBE}") {
                    sh """
                        ${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=FlaskDevSecOps \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.login=${SONAR_QUBE_TOKEN}
                    """
                }
            }

        
        }

    
        stage('Load into Minikube'){
            steps{
                sh "minikube image load ${IMAGE_NAME}"
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}
