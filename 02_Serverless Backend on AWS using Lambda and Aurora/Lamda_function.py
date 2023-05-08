import json
import boto3

rds_client = boto3.client('rds-data')
database_name = 'serverlessdemo'
db_cluster_arn = 'arn:aws:rds:us-east-1:755314965794:cluster:auroraserverlessdemo'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:755314965794:secret:rds-db-credentials/cluster-ONEHQ3WZMFWNXRO75NWMPYL4/admin-XpwER6'

def lambda_handler(event,context):
  response = execute_statement('Select * FROM serverlessdemo.Customers'):
  return response;
Def execute_statement(sql):
  response = rds_client.execute_statement(
    secretArn=db_credentials_secrets_stores_arn,
    response = rds_clientsecrets_store_arn,
    database=database_name,
    resourceArn=db_cluster_arn,
    sql=sql
    
 )
 return response;

  
