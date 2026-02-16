pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main', url: "https://github.com/cubesrepo/curahealthCare-Playwright.git"
            }
        }
        stage('Install dependencies'){
            steps{
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r utilities/requirements.txt
                '''
            }

        }
        stage('Run playwright tests'){
            steps{
                 bat '''
                call venv\\Scripts\\activate
                pytest -v --headless
                '''
            }
        }
    }
}