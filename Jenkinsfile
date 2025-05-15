pipeline {
    agent any

    stages {
        stage('Clone source') {
            steps {
                git url: 'https://github.com/alex-pancho/aqa_090125', branch: 'main'
            }
        }
        stage('Build and activate venv') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'python3 -m pip install -r $WORKSPACE/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest -s -v --junitxml=$WORKSPACE/report.xml'
                junit 'report.xml'
            }
        }
    }
}