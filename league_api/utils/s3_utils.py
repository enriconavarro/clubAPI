import boto3

def send_export(bucket, exports):
    client = boto3.client('s3')
    for export in exports:
        # export[0] = file name
        # export[1] = json_string
        client.put_object(Bucket=bucket, Key=export[0], Body=export[1])
