import boto3
import os

dynamodb = boto3.resource('dynamodb')
answers_table = os.environ['ANSWERS_TABLE']
table = dynamodb.Table(answers_table)

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'user_id': 1,
            'question_id': 1,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'a',
            'created_at' : 1561397870
        }
    )
    batch.put_item(
        Item={
            'user_id': 1,
            'question_id': 2,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'b',
            'created_at': 1558719470
        }
    )
    batch.put_item(
        Item={
            'user_id': 1,
            'question_id': 3,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'c',
            'created_at': 1556127470
        }
    )
    batch.put_item(
        Item={
            'user_id': 1,
            'question_id': 4,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'a',
            'created_at': 1553449070
        }
    )
    batch.put_item(
        Item={
            'user_id': 1,
            'question_id': 6,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'b',
            'created_at': 1551029870

        }
    )
    batch.put_item(
        Item={
            'user_id': 1,
            'question_id': 7,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'c',
            'created_at': 1548351470

        }
    )


    batch.put_item(
        Item={
            'user_id': 2,
            'question_id': 1,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'd',
            'created_at' : 1561397870
        }
    )
    batch.put_item(
        Item={
            'user_id': 2,
            'question_id': 2,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'b',
            'created_at': 1558719470
        }
    )
    batch.put_item(
        Item={
            'user_id': 2,
            'question_id': 3,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'c',
            'created_at': 1556127470
        }
    )
    batch.put_item(
        Item={
            'user_id': 2,
            'question_id': 4,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'd',
            'created_at': 1553449070
        }
    )
    batch.put_item(
        Item={
            'user_id': 2,
            'question_id': 6,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'b',
            'created_at': 1551029870

        }
    )
    batch.put_item(
        Item={
            'user_id': 2,
            'question_id': 7,
            'question_type': 1,
            'form_id' : 1,
            'answer_value' : 'c',
            'created_at': 1548351470

        }
    )