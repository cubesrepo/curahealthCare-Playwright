pipeline{
    agent any

    environment{
        VENV_DIR = "${WORKSPACE}/venv"
    }
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main', url: "https://github.com/cubesrepo/curahealthCare-Playwright.git"
            }
        }
        stage('Install dependencies'){
            steps{
                sh '''
                /Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                pip3 install -r utilities/requirements.txt
                playwright install
                '''
            }

        }
        stage('Run playwright tests'){
            steps{
                sh '''
                source ${VENV_DIR}/bin/activate
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