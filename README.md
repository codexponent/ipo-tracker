# IPO-Tracker
Connecting Siri with AWS Lambda to get IPO fron Nepal Market


# Motivation
Always Searching for the list of IPO from the website is 
kind of a redudant task, why not to use the combination of AWS Lambda and Siri to automate this task for you. Simply User Shortcuts application to make an automation or a voice command to run the application. I have made an application similar to this before which you can check it out here on my [Medium](https://medium.com/swlh/combining-siri-and-aws-lambda-to-get-the-monthly-aws-spending-of-your-account-59be7cb66679?source=user_profile---------3----------------------------) post

# Tools
- AWS Lambda Function
- API Gateway
- Siri

# How to Use
- Copy the code from main.py into the Lambda function that you created and run it
- Also create the trigger 'API Gateway' and make sure to add the URL and API Key into the shortcuts app 

# Steps to make the layer for Lambda function
```bash
mkdir lambda_layers
cd lambda_layers
mkdir python
cd python
pip install requests -t ./
cd ..
zip -r python_modules.zip .
```
