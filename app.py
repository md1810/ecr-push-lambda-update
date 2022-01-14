import boto3
import pandas as pd
import pickle
import lightgbm
BUCKET = 'bucket_name'
FILE_TO_READ = 'pickle_file.pkl'
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket=BUCKET, Key=FILE_TO_READ)
    model = pickle.loads(data['Body'].read())
    data_for_prediction = pd.Series(event).to_frame().T
    res = {'probability': float(model.predict_proba(data_for_prediction)[0][1]),
           'prediction': float(model.predict(data_for_prediction)[0])}
    return res