import pytest
from tools import tools
import json

# test data and defaults
JSON_DATA = '{ "url": "https://www.yahoo.com/news/dog-adopted-7-years-pennsylvania-210548824.html" }'
DATA = json.loads(JSON_DATA)
CONTENT_TYPE ="application/json"

CLEANUP_DATA = '{ "string": "Café au lait is my favorite drink, कॉफ़ी और चाय are delightful too!  "}'

CLEANUP_DATA_RESULT = '{ "string": "Caf au lait is my favorite drink, are delightful too!"}'

DATA = json.loads(CLEANUP_DATA)

@pytest.fixture()
def client():
    client = tools.test_client()
    yield client
    
#def test_encode(client):
#    response = client.get('/encode', data=None, content_type=CONTENT_TYPE)
#    assert b'message' in response.data
#
#
#def test_decode(client):
#    response = client.get('/decode', data=None, content_type=CONTENT_TYPE)
#    assert b'message' in response.data
#
def test_cleanup(client):
    response = client.post('/cleanup', data=CLEANUP_DATA, content_type=CONTENT_TYPE)
    print(response.data)
    cleanup = json.loads(decoded_data.data)['cleanup']
    assert cleanup == CLEANUP_DATA_RESULT

#def test_encode_decode(client):
#    encoded_data = client.post('/encode', data=JSON_DATA, content_type=CONTENT_TYPE)
#    id = json.loads(encoded_data.data)['id']
#    decode_test = '{"id":"'+id+'"}'
#    decoded_data = client.post('/decode', data=decode_test, content_type=CONTENT_TYPE)
#    origin_url = json.loads(decoded_data.data)['original_url']
#    assert origin_url == DATA['url']
#