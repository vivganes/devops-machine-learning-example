pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }

    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
      PATH="C:\\ProgramData\\Anaconda3:$PATH"
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage('Build environment') {
            steps {
                echo "Building virtualenv"
                sh  ''' pip install -r requirements/dev.txt
                    '''
            }
        }



        stage('Unit tests') {
            steps {
                sh  '''  python -m pytest --verbose --junit-xml reports/unit_tests.xml
                    '''
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit allowEmptyResults: true, testResults: 'reports/unit_tests.xml'
                }
            }
        }

        stage('Acceptance tests') {
            steps {
                sh  ''' behave -f=formatters.cucumber_json:PrettyCucumberJSONFormatter -o ./reports/acceptance.json || true
                    '''
            }
            post {
                always {
                    cucumber (buildStatus: 'SUCCESS',
                    fileIncludePattern: '**/*.json',
                    jsonReportDirectory: './reports/',
                  //  parallelTesting: true,
                    sortingMethod: 'ALPHABETICAL')
                }
            }
        }

        stage('Build package') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh  ''' python setup.py bdist_wheel
                    '''
            }
            post {
                always {
                    // Archive unit tests for the future
                    archiveArtifacts allowEmptyArchive: true, artifacts: 'dist/*whl', fingerprint: true
                }
            }
        }

        // stage("Deploy to PyPI") {
        //     steps {
        //         sh """twine upload dist/*
        //         """
        //     }
        // }
    }
}
