@Library("shared") _
pipeline {
    agent { label "Vinod" }
    stages {
        stage("Hello"){
            steps{
                script{
                    hello()
                }
            }
        }
        stage("Code") {
            steps {
                // echo "Cloning the code"
                // git url: "https://github.com/saurabh692/login-signup.git", branch: "main"
                // echo "Code cloning successful"
                script{
                    clone("https://github.com/saurabh692/login-signup.git", "main")
                }
            }
        }

        stage("Build") {
            steps {
                echo "Building the Docker image and running the containers"
                script{
                    docker_build("notes-app","latest")
                }
            }
        }

        stage("Push to Dockerhub") {
            steps {
                script{
                    docker_push("DockerHubCred", "notes-app", "latest")
                }
            }
        }

        stage("Deploy") {
            steps {
                script{
                    // docker_compose()
                    sh "docker compose down && docker compose up --build -d"
                }
                
            }
        }

    }
}
