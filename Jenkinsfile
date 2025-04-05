pipeline {
    agent any
    
    environment {
        REMOTE_HOST = "ec2-user@54.221.127.123"
        PEM_PATH = "/.ssh-keys/docker2-key.pem"
        REPO_URL = "https://github.com/omarvs2003/python-hello-world"
        PROJECT_DIR = "/python-hello-world/python-hello-world/"
        REPOS_DIR = "/python-hello-world/"
    }
    
    stages {
        stage("limpieza") {
            steps {
                sh """
                    cd /
                        sudo ssh -i $PEM_PATH $REMOTE_HOST << EOF 
                            echo "inicio limpieza"
                            echo "Paso: 1 Borrar carpeta existente"
                            
                            sudo rm -rf $PROJECT_DIR
                            
                            echo "Paso: 2 aseguramos que la carpeta de git exista"
                            sudo mkdir -p $REPOS_DIR
                        
                            exit
                        EOF
                """
            }
        }
        stage("clonado") {
            steps {
                sh """
                    cd /
                        sudo ssh -i $PEM_PATH $REMOTE_HOST << EOF 
                            echo "inicio clonado"
                            echo "Paso: 3 clonar git"
                            cd $REPOS_DIR
                            sudo git clone $REPO_URL
                        
                            exit
                        EOF
                """
            }
        }
        stage("contruir rest-api") {
            steps {
                sh """
                    cd /
                        sudo ssh -i $PEM_PATH $REMOTE_HOST << EOF 
                            echo "inicio build"
                            echo "Paso: 4 construir imagen docker"
                            cd $PROJECT_DIR
                            sudo docker build -t hello-image .
                            
                        
                            exit
                        EOF
                """
            }
        }
        stage("correr contenedor") {
            steps {
                sh """
                    cd /
                        sudo ssh -i $PEM_PATH $REMOTE_HOST << EOF 
                            echo "inicio correr contenedor"
                            echo "Paso: 5 crear y correr contenedor docker"
                            cd $PROJECT_DIR
                            sudo docker rm -f hello-container || true
                            
                            sudo docker run --name hello-container -d -p 8090:8090 hello-image
                            
                            exit
                        EOF
                """
            }
        }
        stage("borrar temporales") {
            steps {
                sh """
                    cd /
                        sudo ssh -i $PEM_PATH $REMOTE_HOST << EOF 
                            echo "inicio borrar temporales"
                            echo "Paso: 6 Borrar temporales"
                            
                            sudo rm -rf $PROJECT_DIR
                            
                            exit
                        EOF
                """
            }
        }
         
    }
    
}
