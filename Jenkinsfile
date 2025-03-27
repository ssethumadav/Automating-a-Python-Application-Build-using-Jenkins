pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv ${VENV_DIR}'
                sh '. ${VENV_DIR}/bin/activate && pip install --upgrade pip setuptools wheel'
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. ${VENV_DIR}/bin/activate && pytest'
            }
        }

        stage('Build Artifact') {
            steps {
                sh '. ${VENV_DIR}/bin/activate && python setup.py sdist'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }
}
