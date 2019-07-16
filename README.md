# Capturing table activity with DynamoDB Streams

Work inside your AWS Cloud9 or local environment.

![serverless-dynamodb-item-logs](images/serverless-dynamodb-item-logs.png)

## Configure your environment

* In AWS Cloud9 configure the AWS CLI using the local credentials, and set the region name to **`us-east-1`** and the output format to **`json`**. 

``` bash
aws configure
```
    * AWS Access Key ID: **(Use default)**
    * AWS Secret Access Key: **(Use default)**
    * Default region name [us-east-1]: **us-east-1**
    * Default output format [json]: **json**

* In your local environment [configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration).

## Install dependencies

Update Node.js to the minimal version of 8.

``` bash
nvm i v8
```

Install Serverless CLI tool https://serverless.com/framework/docs/providers/aws/guide/installation/

``` bash
npm install -g serverless
```

## Create a Serverless project

``` bash
git clone https://github.com/aurbac/serverless-dynamodb-item-logs.git
cd serverless-dynamodb-item-logs
```

## Deploy your Serverless project

``` bash
serverless deploy
```

## Testing

``` bash
export ANSWERS_TABLE=serverless_dynamodb_item_logs_dev_answers
python batch_writing.py
```

Wait about 5 minutes and go to Amazon Athena console https://us-east-1.console.aws.amazon.com/athena.