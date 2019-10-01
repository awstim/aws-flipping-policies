import json
import boto3
import datetime
from datetime import datetime as dt
client = boto3.client('iam')

def lambda_handler(event, context):
   
    if (dt.now().minute)/10 == 1  or (dt.now().minute)/10 == 3  or (dt.now().minute)/10 == 5:
        response = client.attach_role_policy(
            RoleName='engineering',
            PolicyArn='arn:aws:iam::aws:policy/job-function/Billing'
        )
        response = client.detach_role_policy(
            RoleName='engineering',
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
        )
        response = client.attach_role_policy(
            RoleName='finance',
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
        )
        response = client.detach_role_policy(
            RoleName='finance',
            PolicyArn='arn:aws:iam::aws:policy/job-function/Billing'
        )
        return {
            'statusCode': 200,
            'body': json.dumps('engineering changed to Billing and finance changed to AdministratorAccess')
        }
    else:
        response = client.attach_role_policy(
            RoleName='engineering',
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
        )
        response = client.detach_role_policy(
            RoleName='engineering',
            PolicyArn='arn:aws:iam::aws:policy/job-function/Billing'
        )
        response = client.attach_role_policy(
            RoleName='finance',
            PolicyArn='arn:aws:iam::aws:policy/job-function/Billing'
        )
        response = client.detach_role_policy(
            RoleName='finance',
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
        )
        return {
            'statusCode': 200,
            'body': json.dumps('engineering changed to AdministratorAccess and finance changed to Billing')
        }
