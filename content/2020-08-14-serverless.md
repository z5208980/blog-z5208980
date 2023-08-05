---
title: "Creating API with AWS Lambda, Express and Serverless (Difficult)"
date: "2020-08-14"
tags: ["Developer"]
image: "https://www.dropbox.com/s/sh8dqgn9ypdrxsf/aws_lambda.png?raw=1"
gradients: ["#e43a15", "#e65245"]
---

### Installing serverless
```bash
# installing serverless
npm install -g serverless
```
This should allow you to use `sls` command in terminal

### Creating AWS Node using sls
```bash
# Create bear bones of
sis create -t aws-nodejs -p folder_name
```

Here it will create two files
- handler.js
- serverless.yml
The `handler.js` file is used to return json files and is the logic of api. Export of the handler name is done here so that the `serverless.yml` file can use it in the function for `lambda`.

```js
module.exports.hello
```
The `serverless.yml` is where like the config ares for the api. The main thing in the file is,

```yml
functions:
    hello: // <- Used for lambda
        handler: handler.hello // <- Called from export
```
More basic structure of what a function in `serverless.yml` would typical look like this,

```yml
projects:
handler: src/api/project.handler
events:
 - http: GET /project

# Path with parameters
# Notice that forcing id param is optional.
# To access param is in the evt
# ie. evt.pathParameteres.id
project:
handler: src/api/project.handler
events:
- http:
path: /project/{id}
method: GET
# request:
#   parameters:
#       id: true
```
Here the `serverless.yml` goes to the handler.js file and calls hello. This is known as a lambda!

```bash
# function
sls invoke local -f function_name
```

So after looking more into serverless, it is just a framework that is used to allow debuging locally and emulates AWS lambda on your local machine. We will be looking more into ExpressJS, as that is what we will be coding in our api.

## AWS Lambda
So, I seen stuff on AWS, such S3, Sagemaker and Lambda, but never actually used one before. This time, its time to dive into AWS, shallowly since we’ll be using serverless to do all the heavy configurations.

In AWS Lambda, when we create a lambda, it can be used to get subscribed from some service. In own cases, since we building an API, it’ll be **API Gateway AWS Proxy**. We can see all the subscriptions to an event through a **testing** button in our lambda.

Basically its, client <–> API-Gateway <–> Server

### Deploying to AWS
In the `serverless.yml`, we will need to include `provider`, `region` and `stage`

```yml
provider:
    name: aws
    runtime: nodejs12.x
    profile: awsName
    region: us-east-1
    stage: dev
```
Then all we need to do is deploy