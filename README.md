## Storing Melbourne weather data in AWS S3 bucket from [OpenWeatherMap](https://openweathermap.org/forecast5) API 

This project fetches Melbourne weather data from the OpenWeatherMap API for Melbourne, Australia, and stores it as a CSV file in an AWS S3 bucket. The project is implemented as a Lambda function that runs on a scheduled basis every 3 hours using EventBridge. Serverless Framework used for making Infrastructure as Code.

---

## Requirements

- Python 3.9
- Serverless framework
- AWS account
- IAM user with programmatic access and administration access permission

---

## Getting started

1. Clone the repository to your local machine
```
git clone https://nandin-b@bitbucket.org/nandin-workspace/data-from-api-to-aws.git
```

2. Install the required dependencies such as serverless-python-requirements, requests, boto3... etc
```
cd data-from-api-to-aws
npm install <dependency name>
```

3. Set up your AWS credentials by setting the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY using AWS CLI.
```
aws configure set aws_access_key_id <your_access_key_id>
aws configure set aws_secret_access_key <your_secret_access_key>
```

4. Deploy the project to AWS
```
sls deploy
```

Once the project is deployed, it will automatically start running every three hours and storing weather data in the S3 bucket.

You can manually invoke the function by running the following command:
```
sls invoke -f store_api_data
```

---

## Structure
The **serverless.yml** file contains the configuration for the project. You can modify this file to change the AWS region, the schedule for running the Lambda function, and other settings.

The **handler.py** file contains the Python code for fetching weather data from the OpenWeatherMap API and storing it in the S3 bucket. You can modify this file to change the API endpoint, the parameters for fetching data, and the format of the data that is stored in the CSV file.

The **requirements.txt** file contains required packages for running project.

---

## Additional information

**These are the steps I took to complete this technical challenge:**

1. Read related AWS white papers to become familiar with the concepts
2. Wrote simple python code to get data from the API
3. Played with the serverless framework to deploy lambda function
4. Converted my simple python code to a lambda function
5. Created a Bitbucket repository and deployed the project
6. Polished up the code
7. Wrote readme.md

**Future improvement ideas:**

1. Split the store_api_data() function into different functions (e.g., get_api_data(), parse_api_data(), store_api_data()) for the reusability.
2. Create .env file to keep api_key
3. Exclude some unnecessary project files for the deployment (e.g., requirements.txt)
4. Reduce the deployment package size
5. Build a pipeline (CI/CD) 

