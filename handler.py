import base64
import json
import gzip
import StringIO
import boto3
import os

def putRecordsToFirehoseStream(streamName, records, client, attemptsMade, maxAttempts):
    failedRecords = []
    codes = []
    errMsg = ''
    # if put_record_batch throws for whatever reason, response['xx'] will error out, adding a check for a valid
    # response will prevent this
    response = None
    try:
        response = client.put_record_batch(DeliveryStreamName=streamName, Records=records)
    except Exception as e:
        failedRecords = records
        errMsg = str(e)

    # if there are no failedRecords (put_record_batch succeeded), iterate over the response to gather results
    if not failedRecords and response and response['FailedPutCount'] > 0:
        for idx, res in enumerate(response['RequestResponses']):
            # (if the result does not have a key 'ErrorCode' OR if it does and is empty) => we do not need to re-ingest
            if 'ErrorCode' not in res or not res['ErrorCode']:
                continue

            codes.append(res['ErrorCode'])
            failedRecords.append(records[idx])

        errMsg = 'Individual error codes: ' + ','.join(codes)

    if len(failedRecords) > 0:
        if attemptsMade + 1 < maxAttempts:
            print('Some records failed while calling PutRecordBatch to Firehose stream, retrying. %s' % (errMsg))
            putRecordsToFirehoseStream(streamName, failedRecords, client, attemptsMade + 1, maxAttempts)
        else:
            raise RuntimeError('Could not put records after %s attempts. %s' % (str(maxAttempts), errMsg))


def makeObjectFromItem(record):
    result = {}
    for key, value in record.items():
        if 'S' in value:
            result[key] = str(value['S'])
        elif 'N' in value:
            result[key] = float(value['N'])
        elif 'BOOL' in value:
            result[key] = value["BOOL"]
        elif 'SS' in value:
            result[key] = value["SS"]
        elif 'M' in value:
            result[key] = makeObjectFromItem(value['M'])
    return result


def sendLogsToFirehose(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    streamName = os.environ['streamName']
    print(json.dumps(event))
    
    records_to_firehose = []
    for record in event['Records']:
        item = {}
        print(record['eventName'])
        if record['eventName']=='MODIFY' or record['eventName']=='INSERT':
            item = makeObjectFromItem(record['dynamodb']['NewImage'])
        else:
            item = makeObjectFromItem(record['dynamodb']['OldImage'])
        item['db_event_name'] = record['eventName']
        item['db_date_time'] = int(record['dynamodb']['ApproximateCreationDateTime'])
        item['user_id'] = int(item['user_id'])
        item['question_id'] = int(item['question_id'])
        item['question_type'] = int(item['question_type'])
        item['form_id'] = int(item['form_id'])
        item['created_at'] = int(item['created_at'])

        if not 'answer_value' in item: item['answer_value'] = ''
        if not 'answer_values' in item: item['answer_values'] = ''
        if not 'answer_value_description' in item: item['answer_value_description'] = ''
        
        item['custom_key'] = str(item['user_id'])+'-'+str(item['question_id'])

        print(json.dumps(item))
        records_to_firehose.append( { 'Data' : json.dumps(item) } )

    if len(records_to_firehose) > 0:
        print(json.dumps(records_to_firehose))
        firehose_client = boto3.client('firehose')
        putRecordsToFirehoseStream(streamName, records_to_firehose, firehose_client, attemptsMade=0, maxAttempts=20)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """