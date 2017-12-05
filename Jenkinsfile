pipeline {
  agent any
  stages {
    stage('TEST') {
      steps {
        sh 'python test.py test'
      }
    }
    stage('PARSE') {
      steps {
        sh 'python test.py parse'
      }
    }
    stage('DEPLOY') {
      steps {
        sh 'python test.py deploy'
      }
    }
  }
}