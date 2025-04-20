import boto3
import json
import pandas as pd
import datetime

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_arn = 'arn:aws:sns:us-east-1:390403896673:s3-daily-data-processing'
date_var = str(datetime.date.today())
print(date_var)
output_bucket='doordash-target-zn-new'
output_file_name = 'processed_data/{}_processed_data.csv'.format(date_var)
print(output_file_name)

def lambda_handler(event, context):
    try:
        input_bucket = event['Records'][0]['s3']['bucket']['name']
        input_file_name = event['Records'][0]['s3']['object']['key']
        res_obj = s3_client.get_object(Bucket=input_bucket,Key=input_file_name)
        data = res_obj['Body'].read().decode('utf-8').split('\r\n')
        print(data)
        print(type(data))
        filter_list = []
        for line in data:
            py_dict = json.loads(line)
            if py_dict['status'] == 'delivered':
                filter_list.append(py_dict)
        print(filter_list)
        df = pd.DataFrame(filter_list)
        print(df.head(7))
        df.to_csv('/tmp/output.csv', index=False)
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(output_bucket)
        print(bucket)
        bucket.upload_file('/tmp/output.csv', output_file_name)

        #Send SNS Notification
        sns_client.publish(
            TopicArn=sns_arn,
            Message='Data Processing Completed for {} and it has been stored in {} '.format(output_file_name,output_bucket),
            Subject='Data Processing Completed'
        )
    except Exception as e:
        print(str(e))
        sns_client.publish(
            TopicArn=sns_arn,
            Message='Data Processing Failed for {}'.format(output_file_name),
            Subject='Data Processing Failed'
        )



