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
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip3 install --upgrade pip
                pip3 install -r utilities/requirements.txt
                playwright install
                '''
            }

        }
        stage('Run playwright tests'){
            steps{
                sh '''
                source venv/bin/activate
                pytest -v --alluredir=reports/allure-results
                '''
            }
        }
    }
    post{
        always{
            echo "Generating allure report"
            step([$class: 'AllureReportPublisher',
                  results: [[path: 'reports/allure-results']],
                  includeProperties: false,
                  jdk: ''
            ])
            echo "Cleaning up workspace"
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