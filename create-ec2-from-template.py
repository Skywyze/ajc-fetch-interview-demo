import boto3



ec2 = boto3.client('ec2')
desc_resp = ec2.describe_instances()
print(desc_resp)

