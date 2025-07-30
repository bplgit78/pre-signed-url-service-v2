Pre-Signed URL Upload Service
A serverless AWS service for generating pre-signed S3 URLs via a REST API. Clients can upload documents securely and directly to S3 without needing AWS credentials.

🚀 What This Repo Accomplishes
Lambda Function for generating S3 pre-signed PUT URLs

API Gateway (REST API) endpoint (POST /upload) that invokes the Lambda function

S3 Bucket for receiving uploads (configured separately)

CI/CD Pipeline powered by GitHub Actions using AWS SAM

Infrastructure as Code via template.yaml (SAM / CloudFormation)

Secure and scalable serverless architecture for document ingestion

🧱 6-Step System Flow
Client requests a pre-signed upload URL via the API

API Gateway triggers the Lambda function

Lambda validates the input and generates a signed URL

The URL is returned to the client

Client uploads the file directly to S3 using the signed URL

S3 bucket is configured to auto-delete files via lifecycle policies

📁 Repo Structure

pre-signed-url-service/
├── lambda/
│   └── lambda_function.py      # Lambda logic
├── template.yaml               # SAM template defining Lambda & API
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD pipeline
└── README.md                   # Project overview & instructions

🛠️ How to Get Started
Prerequisites
AWS account with permissions for S3, Lambda, CloudFormation, API Gateway

GitHub account for CI/CD

AWS CLI and AWS SAM CLI installed

Setup Instructions
Clone the repository


git clone https://github.com/your-org/pre-signed-url-service.git
cd pre-signed-url-service
Create the S3 bucket (if not existing):


aws s3api create-bucket \
  --bucket pre_signed_url_user_doc_images \
  --region us-east-1
Push to GitHub and configure Secrets

Add the repository to GitHub

In Settings → Secrets → Actions, add:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

Commit and push to main


git add .
git commit -m "Initial commit"
git push -u origin main
This triggers GitHub Actions to build and deploy the stack automatically.

Verify Deployment

Navigate to the AWS console → CloudFormation → confirm PreSignedUrlStack exists

Confirm API Gateway endpoint and Lambda function exist

Test the API


curl -X POST https://<api-id>.execute-api.[region].amazonaws.com/prod/upload \
  -H "Content-Type: application/json" \
  -d '{"file_name": "id.png", "profile_exists": true, "user_id": "user123"}'
⚙️ Topics for Future Expansion
Request validation and authentication (e.g., JWT, Cognito)

S3 event trigger for document processing (OCR, tokenization)

DynamoDB integration for storing tokens and age info

Lifecycle policies and cleanup workflows

Enhanced CI/CD pipelines (test environments, multi-stage deploys)

🩺 Contributing / Branch Strategy
Feature branches for new additions (e.g. feature/dynamodb-integration)

Create a Pull Request and request review before merging

main is always deployable and CI-tested

📄 License
For private use only—no licensing restrictions.