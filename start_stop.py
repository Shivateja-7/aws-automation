import boto3
from datetime import datetime, timezone

ec2 = boto3.client('ec2')

instance_resources = ec2.describe_instances(Filters=[{'Name': 'tag:Environment', 'Values': ['Dev']}])

current_hour = datetime.now(timezone.utc).hour

for reservation in instance_resources['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        if 9 <= current_hour < 19:
            ec2.start_instances(InstanceIds=[instance_id])
        else:
            ec2.stop_instances(InstanceIds=[instance_id])