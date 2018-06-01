import boto3
import sys
import time
from datetime import datetime, timedelta

client = boto3.client('cloudwatch', region_name = 'us-east-2')
response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': 'i-000eb85bb35a2f5dd'
                },
        ],
        StartTime=datetime(2018, 5, 01) - timedelta(seconds=600),
        EndTime=datetime(2018, 5, 29),
        Period=86400,
        Statistics=['Average',
        ],
        Unit='Percent'
)
#print(response)
time.sleep(10)
for cpu in response['Datapoints']:
  print(cpu)

