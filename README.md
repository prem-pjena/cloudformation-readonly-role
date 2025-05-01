# AWS ReadOnlyAccess CloudFormation & Inventory Fetcher

This project includes a CloudFormation template and a Python script to create a stack with **read-only IAM access** to common AWS services and dynamically fetch resource inventory using **boto3**.

---

## 📁 Contents

- `readonly-role.yml` – CloudFormation template to create a read-only IAM Role.
- `fetch_stack_inventory.py` – Python script to fetch stack resources and list inventory (EC2, S3).
- `README.md` – Documentation on usage and setup.

---

## 🚀 CloudFormation Stack Deployment

### 1. Upload Template
Ensure the `readonly-role.yml` is publicly accessible via S3.

### 2. Launch the Stack
Use the following Launch Stack URL to deploy the CloudFormation stack:

https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://yml-python.s3.amazonaws.com/readonly-role.yml&stackName=ReadOnlyAccessStack


### 3. Confirm Successful Stack Creation
After launching, verify the stack status is `CREATE_COMPLETE` in the CloudFormation Console.

---

## 🐍 Python Script: Fetch Inventory

### Requirements

- Python 3.6+
- `boto3` library (`pip install boto3`)
- Must run in an **IAM Role / Instance Profile** with sufficient permissions (no access keys used)

### Usage

```bash
python3 fetch_stack_inventory.py

Script Output
✅ Stack creation status

📦 IAM Role created

🖥️ EC2 Instances (if any)

🪣 S3 Buckets (if any)

Fetching stack resources for: ReadOnlyAccessStack

✅ Stack 'ReadOnlyAccessStack' status: CREATE_COMPLETE
- AWS::IAM::Role: ReadOnlyAccessRole

🔍 EC2 Instances:

🔍 S3 Buckets:
  - Bucket Name: yml-python

🔐 Security Notes
No credentials are hardcoded.

CloudFormation template and bucket policy allow read-only public access for CloudFormation.

Make sure to restrict access once the stack is created if no longer needed.

🧑‍💻 Author
Prem Prakash Jena
GitHub | LinkedIn
Email: premprakashjena04@gmail.com

📌 License
MIT License
