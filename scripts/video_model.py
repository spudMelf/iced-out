# Imports
import requests 
from dotenv import load_dotenv
import os

load_dotenv()

api_key =  os.getenv('HIVE_MIND_KEY')


def handle_hive_response(response_dict):
   # Parse model response JSON and use model results for moderation.
   # See a basic example implementation in the last section.
   pass

def moderate_post_sync(content_url):
   # Example Request (visual, synchronous endpoint, content hosted at URL):
   headers = {'Authorization': f'Token {api_key}'} # Example for visual moderation tasks
   data = {'url': content_url} # This is also where you would add metadata if desired
   model_response = requests.post('https://api.thehive.ai/api/v2/task/sync', headers=headers, data=data)
   response_dict = model_response.json()
   handle_hive_response(response_dict)