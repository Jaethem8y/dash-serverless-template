# dash-serverless-template

## What you need

- Node JS
- Docker daemon running

## Steps

- get all the dependencies to requirements.txt (Example requirements.txt should have most of it already)
- pip intsall serverless-wsgi
- pip install serverless-python-requirements
- configure serverless on  your side (follow tutorials online to do so)
- install npm packages that are needed : serverless and etc
- run: sls wsgi serve :: to see if it runs locally fine
- run: sls deploy :: to deploy your app on S3 lambda and api gateway
