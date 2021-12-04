
pipeline {
    agent any
    stages{
        stage('Desplegar servicio') {
            steps{
                sh'''apt install python3-pip -y'''
                sh'''pip install -r requirements.txt'''
                sh'''python3 manage.py runserver > output.txt &'''
                sh'''sleep 1m'''
            }
        }
        stage('Lanzar curl') {
            steps{
                sh'''curl -XPUT --request GET "http://127.0.0.1:8000/free_spaces/" --data-raw "{'time':7200,'period':75}"
                '''
            }
        }
    }
}