# Cheat Sheet for creating Python app with Watson Personality Insights.

1. Download Cloudfoundry CLI: https://github.com/cloudfoundry/cli/releases  We will use this to communicate with Bluemix from our laptop console.
2. Sign up to Bluemix: http://bluemix.net
3. Launch Python Buildpack: https://console.ng.bluemix.net/catalog/starters/python/?taxonomyNavigation=apps
4. From resulting Python Window: Download Starter Code to your local drive

~~~~
<DIR>          .
<DIR>          ..
            34 CHANGELOG.md
           142 manifest.yml
            22 Procfile
           393 README.md
             0 requirements.txt
           594 server.py
            74 service.cmd
<DIR>          static
~~~~

5. Review the manmifest.yml file.
~~~~
applications:
- path: .
  memory: 128M
  instances: 1
  domain: mybluemix.net
  name: Berkeley1
  host: Berkeley1
  disk_quota: 1024M
~~~~
6. Check out Watson Personality Insights: https://personality-insights-livedemo.mybluemix.net/
7. In your console window: Create personality insights service: cf create-service personality_insights tiered personality_insights_service
8. In manifest.yml file in starter code on your local drive, add services: tag and actual service and line below.
9. Also, change name: and host: to unique names 
~~~~
applications:
- path: .
  memory: 128M
  instances: 1
  domain: mybluemix.net
  name: Berkeley1
  host: Berkeley1
  disk_quota: 1024M
  services:
  - personality-insights-service
~~~~
10. Do ***cf push*** in cour console window on your laptop in order to upload your modified code to Bluemix.
11.
12.
