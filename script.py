import requests
import json

def run_graphql_query(endpoint, query):
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
  }

  data = {'query': query}

  try:
    response = requests.post(endpoint, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
  except requests.exceptions.ConnectionError as errt:
    print(f"Error Connecting: {errc}")
  except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
  except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")

if __name__ == "__main__":
  graphql_endpoint = 'YOUR_GRAPHQL_ENDPOINT'

graphql_query = '''
    {
        example {
            field1
            field2
        }
    }
    '''

result = run_graphql_query(graphql_endpoint, graphql_query)
print(json.dumps(result, indent=2))
