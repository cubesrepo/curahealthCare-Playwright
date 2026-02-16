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
                playwright install
                '''
            }

        }
        stage('Run playwright tests'){
            steps{
                bat '''
                call venv\\Scripts\\activate
                pytest -v --alluredir=reports/allure-results
                '''
            }
        }
    }
    post{
        always{
            echo "Generating allure report"
            allure([
                includeProperties: false,
                jdk: '',
                results [[path: 'reports/allure-results']]
            ])
            echo "cleaning up workspace"
            cleanWs()
        }
        success{
            echo "Test passed successfully"
        }
        failure{
            echo "Test failed!"
        }
    }
}