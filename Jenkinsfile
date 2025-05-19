pipeline {
    agent any

    stages {
        stage("Clean workspace") {
            steps {
                sh "rm -rf ./*"
            }
        }

        stage("Checkout") {
            steps {
                git url: 'https://github.com/ByJeanCa/web-app-test', credentialsId: 'git-cred', branch: 'main'
            }
        }

        stage("Testing code") {
            steps {
                sh "docker compose -f compose_test.yml up --build --abort-on-container-exit"
                sh "docker compose -f compose_test.yml down"
            }
        }
        stage("Deploy") {
         //  when {
         //     branch 'main'
        //   }
            steps {
                withCredentials([string(credentialsId: 'awx-cred', variable: 'AWS_TOKEN')]) {
                    sh '''
                    curl -k -X POST "http://host.docker.internal:8081/api/v2/job_templates/47/launch/" \\
                         -H "Content-Type: application/json" \\
                         -H "Authorization: Bearer ${AWS_TOKEN}"
                    '''
                }
            }
        }
    }
}
