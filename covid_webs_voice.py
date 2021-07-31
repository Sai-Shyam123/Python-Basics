import requests
import json

API_KEY = 'taOkvhXAUOi5'
PROJECT_TOKEN = 'toDXMYPmrwnz'
RUN_TOKEN = 't44cXG7xtX6r'

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={'api_key': API_KEY})
data = json.loads(response.text)
print(data)

# 16:54