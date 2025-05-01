# AWS CloudFormation ReadOnly Role Stack + Inventory Fetcher

## Stack Launch

Launch the CloudFormation stack here:  
[Launch Stack](https://console.aws.amazon.com/cloudformation/home?#/stacks/create/review?templateURL=https://raw.githubusercontent.com/prem-pjena/cloudformation-readonly-role/main/readonly-role.yml&stackName=ReadOnlyAccessStack)

## Python Inventory Script

This script fetches inventory info (e.g., EC2, S3) from resources created by the stack.

### Requirements

- Python 3.x
- `boto3` installed (`pip install boto3`)
- Must run in an AWS environment with IAM permissions (EC2 instance with a role or AWS CloudShell)

### Usage

```bash
python fetch_stack_inventory.py ReadOnlyAccessStack
