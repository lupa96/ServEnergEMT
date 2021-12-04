
pipeline {
    agent any
    stages{
        stage('Desplegar servicio') {
            steps{
                sh'''python3 manage.py runserver'''
            }
        }
        stage('Lanzar curl') {
            steps{
                sh'''curl --location --request GET 'http://127.0.0.1:8000/free_spaces/'
                --header 'Content-Type: application/json'
                --data-raw '{"time": 75,"period":  75}'
                '''
            }
        }
    }
}