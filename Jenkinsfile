pipeline {
    agent { dockerfile {
                args '-u root'
                additionalBuildArgs  '--build-arg PYTHON_VERSION=2'
            }
    }

    triggers { pollSCM('*/1 * * * 1-5') }

    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    /*
    environment {
        REDPITAYA_HOSTNAME = "root"
        REDPITAYA_PASSWORD = "root"
    }
    */

    stages {
        stage('Test docker environment') {
            steps {
                sh  ''' python -V
                        echo $USER
                        groups
                        id
                    '''
            }
        }

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage('Build environment') {
            steps {
                echo "Building virtualenv"
                sh ''' python setup.py install
                   '''
            }
        }

        stage('Static code metrics') {
            steps {
                echo "Raw metrics"
                sh  ''' radon raw --json pysine > raw_report.json
                        radon cc --json pysine > cc_report.json
                        radon mi --json pysine > mi_report.json
                        sloccount --duplicates --wide pysine > sloccount.sc
                    '''
                echo "Test coverage"
                sh  ''' coverage run pysine 1 1 2 3
                        python -m coverage xml -o reports/coverage.xml
                    '''
                echo "Style check"
                sh  ''' pylint pysine || true
                    '''
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }



        stage('Unit tests') {
            steps {
                sh  ''' nosetests --with-xunit --xunit-file=reports/xunit.xml
                    '''
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit allowEmptyResults: true, testResults: 'reports/unit_tests.xml'
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
        //            """
        //     }
        // }
    }

    post {
        //always {
        //    sh 'conda remove --yes -n ${BUILD_TAG} --all'
        //}
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']])
        }
    }
}