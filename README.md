
# AWS ReadOnlyAccess CloudFormation & Resource Fetch Script

This project demonstrates how to create an IAM Role with read-only permissions using AWS CloudFormation and dynamically fetch AWS resource inventory (EC2 and S3) using a Python script.

## 📁 Files Included

- **`readonly-role.yml`**: CloudFormation template to create the IAM role with read-only access to EC2 and S3.
- **`fetch_stack_inventory.py`**: Python script to fetch EC2 and S3 resources after stack creation.
- **`README.md`**: Instructions and documentation on how to use the CloudFormation template and the Python script.

## 🛠 How to Use

### Step 1: Upload the YAML Template

Upload the `readonly-role.yml` CloudFormation template to an S3 bucket and make it publicly accessible for CloudFormation to use. For example, upload the file to `yml-python` bucket.

### Step 2: Deploy CloudFormation Stack

To create the IAM role with read-only permissions, use the following Launch Stack URL:

👉 [Launch Stack in AWS](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://yml-python.s3.amazonaws.com/readonly-role.yml&stackName=ReadOnlyAccessStack)

This will create the **ReadOnlyAccessRole** in your AWS account with read-only access to EC2, S3, and other resources.

### Step 3: Run the Python Script

Make sure your environment (EC2, Lambda, or your local machine) is configured with the appropriate IAM permissions and roles to allow access to CloudFormation, EC2, and S3 resources.

To fetch inventory details of resources in the stack, run the Python script:

1. **Install dependencies**:
   Make sure you have Python 3.6+ and the `boto3` library installed. Install `boto3` using pip:

   ```bash
   pip install boto3
   ```

2. **Run the Python script**:

   ```bash
   python3 fetch_stack_inventory.py
   ```

   **Expected Output**:

   ```bash
   Fetching stack resources for: ReadOnlyAccessStack

   ✅ Stack 'ReadOnlyAccessStack' status: CREATE_COMPLETE
   - AWS::IAM::Role: ReadOnlyAccessRole

   🔍 EC2 Instances:
     - Instance ID: i-1234567890abcdef0 | State: running

   🔍 S3 Buckets:
     - Bucket Name: yml-python
   ```

The script will output the EC2 instances and S3 buckets created by the CloudFormation stack, based on the resources associated with the stack.

---

## ✅ Requirements

- **Python 3.6+**
- **boto3** (install via `pip install boto3`)

### AWS IAM Permissions

- The script assumes IAM permissions from the environment, such as EC2 Instance Profiles or Lambda Execution Role.
- No explicit credentials (access keys or secret keys) are used or hardcoded in the script.

---

## 🔐 Security Note

The script does **not store** or **pass** any credentials explicitly. IAM permissions are assumed from the environment in which the script runs, such as an EC2 instance or Lambda function that has the appropriate IAM role attached.

### Ensure the following permissions are granted:

- **CloudFormation**: `DescribeStacks`, `DescribeStackResources`
- **EC2**: `DescribeInstances`
- **S3**: `ListBuckets`

---

## 👤 Author

**Prem Prakash Jena**  
GitHub: [prem-pjena](https://github.com/prem-pjena)  
Portfolio: [devops-portfolio-five.vercel.app](https://devops-portfolio-five.vercel.app/)

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

- The CloudFormation template (`readonly-role.yml`) creates a role with read-only permissions for several AWS services.
- The Python script assumes IAM permissions from the execution environment (EC2, Lambda, etc.) and fetches inventory details for EC2 and S3 resources.
