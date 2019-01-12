#!groovy


pipeline {
    triggers { pollSCM('*/1 * * * *') }

    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }


    environment {
        REDPITAYA_HOSTNAME = "root"
        REDPITAYA_PASSWORD = "root"
    }

    agent none

    stages {
        stage ("Code pull"){
            agent any
            steps{
                checkout scm
                stash 'source'
                unstash 'source'
                }}
        stage('PRE-UNIT-TEST') {
            agent { dockerfile { args '-u root'
                                 additionalBuildArgs  '--build-arg PYTHON_VERSION=3' }}
            stages {
                stage('Docker environment diagnostics') { steps {
                    sh  ''' which python
                            python -V
                            echo $PYTHON_VERSION
                            '''
                }}
                stage('Build environment') { steps {
                    echo "Building virtualenv"
                    unstash 'source'
                    sh 'python setup.py install'
                }}
                stage('Static code metrics') { steps {
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
                post{ always { step(
                    [ $class: 'CoberturaPublisher',
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
                }}}
        }}

        stage('Unit tests') {
            agent { dockerfile { args '-u root'
                                 additionalBuildArgs  '--build-arg PYTHON_VERSION=3' }}
            steps {
                unstash 'source'
                sh 'python setup.py install'
                sh 'nosetests --with-xunit --xunit-file=reports/xunit.xml' }
            post { always {
                // Archive unit tests for the future
                junit allowEmptyResults: true, testResults: 'reports/unit_tests.xml' }}}

        stage('Build and deploy package') {
            agent { dockerfile { args '-u root'
                         additionalBuildArgs  '--build-arg PYTHON_VERSION=3' }}
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS'}}
            steps {
                unstash 'source'
                sh 'python setup.py install'
                sh  ''' python setup.py bdist_wheel
                        //twine upload dist/*
                    ''' }
            post { always {
                // Archive unit tests for the future
                archiveArtifacts allowEmptyArchive: true, artifacts: 'dist/*whl', fingerprint: true}}}
        }
        post { failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: "pyrpl.readthedocs.io@gmail.com"
                ) }
    }
}

