pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                git "https://github.com/cubesrepo/curahealthCare-Playwright.git"
            }
        }
        stage('Install dependencies'){
            bat '''
            python -m venv venv
            call venv\\Scripts\\activate
            pip install -r utilities/requirements.txt
            '''
        }
        stage('Run playwright tests'){
            bat '''
            call venv\\Scripts\\activate
            pytest -v --headless
            '''
        }
    }
}