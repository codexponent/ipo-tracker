# IPO-Tracker
Connecting Siri with AWS Lambda to get IPO fron Nepal Market


# Motivation
Always searching for the list of IPOs from the website is kind of a redundant task, why not use the combination of AWS Lambda and Siri to automate this task for you. Simply use the Shortcuts application to make automation or a voice command to run the application. I have made an application similar to this before which you can check out here on my [GitHub](https://github.com/codexponent/siri-lambda) and its subsequent post on [Medium](https://medium.com/swlh/combining-siri-and-aws-lambda-to-get-the-monthly-aws-spending-of-your-account-59be7cb66679?source=user_profile---------3----------------------------) post.

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
