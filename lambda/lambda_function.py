import json
import boto3
import uuid
import random
import time
from datetime import datetime, timedelta

def generate_fake_data():
    user_id = random.randint(0, 1000)
    session_id = str(random.randint(1500000000000000, 1600000000000000))
    session_start = int((datetime.now() - timedelta(days=random.randint(0, 10))).timestamp() * 1000)
    session_size = random.randint(1, 10)
    click_article_id = random.randint(1, 10000)

    # Generate a click_timestamp between now and 5 days ago
    now = datetime.now()
    start_time = now - timedelta(days=5)
    click_timestamp = random.randint(int(start_time.timestamp() * 1000), int(now.timestamp() * 1000))

    click_environment = random.randint(1, 5)
    click_deviceGroup = random.randint(1, 4)
    click_os = random.randint(1, 30)
    click_country = random.randint(1, 200)
    click_region = random.randint(1, 50)
    click_referrer_type = random.randint(1, 7)

    data = {
        "user_id": user_id,
        "session_id": session_id,
        "session_start": session_start,
        "session_size": session_size,
        "click_article_id": click_article_id,
        "click_timestamp": click_timestamp,
        "click_environment": click_environment,
        "click_deviceGroup": click_deviceGroup,
        "click_os": click_os,
        "click_country": click_country,
        "click_region": click_region,
        "click_referrer_type": click_referrer_type
    }
    
    return data

def lambda_handler(event, context):
    client = boto3.client('kinesis')
    start_time = time.time()
    duration = 50  # Duration in seconds
    
    while time.time() - start_time < duration:
        data = generate_fake_data()
        
        response = client.put_record(
            StreamName='birds',
            Data=json.dumps(data),
            PartitionKey=str(uuid.uuid4())
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent fake data to Kinesis for 50 seconds')
    }
