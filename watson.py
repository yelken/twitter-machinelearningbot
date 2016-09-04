#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username='1bf7ab63-da73-468d-8622-d820ff2e242b',
  password='AlDs0JM3B3CI',
  version='2016-07-11'
)

# Replace with the context obtained from the initial request
context = {}

workspace_id = '08cf1573-abbc-4ced-881d-326a95172d75'

response = conversation.message(
  workspace_id=workspace_id,
  message_input={'text': 'dilma bolada'},
  context=context
)

print(response['output']['text'][0])
print(response['context'])
print(json.dumps(response, indent=2))