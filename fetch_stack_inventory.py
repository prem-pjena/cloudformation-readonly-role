import boto3

def fetch_resources_from_stack(stack_name):
    # Use default credentials (from instance role or AWS environment)
    cf = boto3.client('cloudformation')
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    print(f"Fetching stack resources for: {stack_name}")
    
    try:
        # Get stack details
        stack = cf.describe_stacks(StackName=stack_name)['Stacks'][0]
        print(f"\n✅ Stack '{stack_name}' status: {stack['StackStatus']}")

        # Get physical resources associated with the stack
        resources = cf.describe_stack_resources(StackName=stack_name)['StackResources']
        for res in resources:
            print(f"- {res['ResourceType']}: {res['PhysicalResourceId']}")

        # Fetch EC2 instances
        print("\n🔍 EC2 Instances:")
        instances = ec2.describe_instances()
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                print(f"  - Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

        # Fetch S3 buckets
        print("\n🔍 S3 Buckets:")
        buckets = s3.list_buckets()
        for bucket in buckets['Buckets']:
            print(f"  - Bucket Name: {bucket['Name']}")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    stack_name = "ReadOnlyAccessStack"  # Replace with your actual stack name
    fetch_resources_from_stack(stack_name)
