# AWS ReadOnlyAccess CloudFormation & Resource Fetch Script

This project demonstrates how to create an IAM Role with read-only permissions using CloudFormation and dynamically fetch AWS resource inventory using a Python script.

---

## 📁 Files Included

- `readonly-role.yml`: CloudFormation template to create the IAM role.
- `fetch_stack_inventory.py`: Python script to list EC2 and S3 resources after stack creation.
- `README.md`: Instructions and documentation.

---

## 🛠 How to Use

### Step 1: Upload the YAML Template

Upload `readonly-role.yml` to an S3 bucket (e.g., `yml-python`) and make it publicly accessible for CloudFormation.

### Step 2: Deploy CloudFormation Stack

Use the Launch Stack URL below to create the IAM role:

👉 [Launch Stack in AWS](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://yml-python.s3.amazonaws.com/readonly-role.yml&stackName=ReadOnlyAccessStack)

### Step 3: Run the Python Script

Ensure your environment (EC2, Lambda, or local machine with IAM role) has permission to access CloudFormation, EC2, and S3.

Run the script:

```bash
python3 fetch_stack_inventory.py

Fetching stack resources for: ReadOnlyAccessStack

✅ Stack 'ReadOnlyAccessStack' status: CREATE_COMPLETE
- AWS::IAM::Role: ReadOnlyAccessRole

🔍 EC2 Instances:
  - Instance ID: i-1234567890abcdef0 | State: running

🔍 S3 Buckets:
  - Bucket Name: yml-python

✅ Requirements
Python 3.6+

boto3 (pip install boto3)

AWS IAM Role or EC2 Instance Profile with permissions (no access key used)

🔐 Security Note
No credentials are stored or passed in the script. IAM permissions are assumed from the execution environment.

👤 Author
Prem Prakash Jena
GitHub | Portfolio

