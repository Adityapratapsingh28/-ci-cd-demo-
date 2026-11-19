pipeline {
    agent any

    environment {
        DOCKERHUB_USER  = 'bella38'
        APP_NAME        = 'ci-cd-demo'
        IMAGE_TAG       = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Adityapratapsingh28/-ci-cd-demo-.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USER/$APP_NAME:$IMAGE_TAG -t $DOCKERHUB_USER/$APP_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh 'echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin'
                    sh 'docker push $DOCKERHUB_USER/$APP_NAME:$IMAGE_TAG'
                    sh 'docker push $DOCKERHUB_USER/$APP_NAME:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-demo', variable: 'KUBECONFIG')]) {
                    sh 'kubectl set image deployment/ci-cd-demo ci-cd-demo=$DOCKERHUB_USER/$APP_NAME:$IMAGE_TAG --record || kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl rollout status deployment/ci-cd-demo --timeout=120s'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployed version $IMAGE_TAG successfully!"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
