import os
import boto3
from dotenv import dotenv_values

YOUR_ID = '19'


def upload_to_yandex_cloud(file_path, aws_access_key_id, aws_secret_access_key):
    client = boto3.client(
        's3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    bucket_name = 'pabd24'
    object_name = f'{YOUR_ID}/' + os.path.basename(file_path)
    client.upload_file(file_path, bucket_name, object_name)


def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    config = dotenv_values(dotenv_path)
    folder_path = r'C:\Users\7ivan\PycharmProjects\pabd24\data\raw'

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            upload_to_yandex_cloud(file_path, config['KEY'], config['SECRET'])


if __name__ == '__main__':
    main()
