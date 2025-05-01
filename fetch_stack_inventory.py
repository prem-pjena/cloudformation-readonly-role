import boto3
import sys

def fetch_resources_from_stack(stack_name):
    """
    Fetch all resources created by the specified CloudFormation stack
    and print basic inventory info (EC2, S3).
    """
    # Initialize CloudFormation client using instance profile / assumed role (no credentials in code)
    cf_client = boto3.client('cloudformation')
    
    try:
        # Describe stack resources
        response = cf_client.describe_stack_resources(StackName=stack_name)
        resources = response['StackResources']
        
        ec2_ids = []
        s3_buckets = []

        # Identify resource types
        for res in resources:
            if res['ResourceType'] == 'AWS::EC2::Instance':
                ec2_ids.append(res['PhysicalResourceId'])
            elif res['ResourceType'] == 'AWS::S3::Bucket':
                s3_buckets.append(res['PhysicalResourceId'])

        # Print EC2 instance details
        if ec2_ids:
            print(f"\nFound {len(ec2_ids)} EC2 instance(s):")
            ec2_client = boto3.client('ec2')
            ec2_response = ec2_client.describe_instances(InstanceIds=ec2_ids)
            for reservation in ec2_response['Reservations']:
                for instance in reservation['Instances']:
                    print(f"  - ID: {instance['InstanceId']}, Type: {instance['InstanceType']}, State: {instance['State']['Name']}")
        else:
            print("\nNo EC2 instances found.")

        # Print S3 bucket names
        if s3_buckets:
            print(f"\nFound {len(s3_buckets)} S3 bucket(s):")
            for bucket in s3_buckets:
                print(f"  - Bucket Name: {bucket}")
        else:
            print("\nNo S3 buckets found.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_stack_inventory.py <StackName or StackARN>")
    else:
        fetch_resources_from_stack(sys.argv[1])
