import boto3

def create_tables():
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

    # Create Users table
    try:
        users_table = dynamodb.create_table(
            TableName='Users',
            KeySchema=[
                {'AttributeName': 'username', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'username', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("Creating Users table...")
        users_table.meta.client.get_waiter('table_exists').wait(TableName='Users')
        print("Users table created successfully!")
    except Exception as e:
        print(f"Users table creation failed (or already exists): {e}")

    # Create Orders table
    try:
        orders_table = dynamodb.create_table(
            TableName='Orders',
            KeySchema=[
                {'AttributeName': 'order_id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'order_id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("Creating Orders table...")
        orders_table.meta.client.get_waiter('table_exists').wait(TableName='Orders')
        print("Orders table created successfully!")
    except Exception as e:
        print(f"Orders table creation failed (or already exists): {e}")

if __name__ == '__main__':
    create_tables()
