pipeline {
    agent none

    environment {
        HOME = '.'
    }

    options { disableConcurrentBuilds() }

    stages {
        stage ('Build and Test' ) {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }

            stages {
                stage ('Build') {
                    steps {
                        sh './scripts/build.sh'
                    }
                }

                stage ('Test') {
                    steps {
                        sh './scripts/test.sh'
                    }
                }

                stage ('Clean'){
                    steps {
                        sh 'rm -rf venv'
                    }
                }
            }
        }

        stage ('Build and Package') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                    reuseNode false
                }
            }

            stages {
                stage ('Build') {
                    steps {
                        sh './scripts/build_package.sh'
                    }
                }

                stage ('Package') {
                    steps {
                        sh './scripts/package.sh echo $?'
                        stash name: 'build-output', includes: 'package.zip'
                    }
                }

                stage ('Clean'){
                    steps {
                        sh 'rm -rf venv'
                    }
                }
            }
        }

        stage ('Release') {
            agent any

            when {
                branch 'master'
            }

            steps {
                unstash 'build-output'

                sh 'cosmos-release lambda --lambda-version=`python3 setup.py --version` ./package.zip efficient-learning-lambda'
            }
        }

        stage ('Deploy to Test') {
            agent any

            when {
                branch 'master'
            }

            steps {
                unstash 'build-output'

                sh 'cosmos deploy-lambda -f -r `python3 setup.py --version` efficient-learning-lambda test'
            }
        }
    }
}