#!/usr/bin/env python3

import requests
import json

web_hook_url = 'https://hooks.slack.com/services/xxxxxxxxxxxxxxxx'
slack_msg = {'text': 'Python-Slack-Test von Bernd'}

requests.post(web_hook_url, data=json.dumps(slack_msg))
