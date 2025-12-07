import boto3

s3 = boto3.client('s3')

for bucket in s3.list_buckets()['Buckets']:
    acl = s3.get_bucket_acl(Bucket=bucket['Name'])
    for grant in acl['Grants']:
        if 'AllUsers' in str(grant['Grantee']):
            print(f"Public bucket found: {bucket['Name']}")