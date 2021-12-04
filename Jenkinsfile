
pipeline {
    agent any
    stages{
        stage('EMT parra') {
            steps{
                sh'''python3 manage.py runserver'''
            }
        }
        stage('EMT parra') {
            steps{
                sh'''python3 manage.py runserver'''
            }
            steps{
                sh'''curl --location --request GET 'http://127.0.0.1:8000/free_spaces/'
                --header 'Content-Type: application/json'
                --data-raw '{"time": 7200,"period":  75}'
                '''
            }
        }
    }
}