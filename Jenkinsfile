def dockerImage

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "shaurya1607/comicnerd"
        KUBECONFIG = "/var/lib/jenkins/.kube/config"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(
                        "${DOCKER_IMAGE}:build-${BUILD_NUMBER}"
                    )
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry(
                        'https://index.docker.io/v1/',
                        'dockerhub-credentials'
                    ) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                    kubectl --kubeconfig=${KUBECONFIG} \
                    -n comicnerd \
                    set image deployment/comicnerd \
                    comicnerd=${DOCKER_IMAGE}:build-${BUILD_NUMBER}
                """
            }
        }

        stage('Verify Deployment') {
            steps {
                sh """
                    kubectl --kubeconfig=${KUBECONFIG} \
                    rollout status deployment/comicnerd \
                    -n comicnerd \
                    --timeout=180s
                """
            }
        }
    }

    post {
        success {
            echo "ComicNerd CI/CD pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed. Check the Jenkins console output."
        }
    }
}
