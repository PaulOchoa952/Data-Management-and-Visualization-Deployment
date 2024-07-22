import requests
import csv
metabase_url = 'http://localhost:31111'
login_endpoint = f'{metabase_url}/api/session'
login_payload = {
    'username': 'paalochoame@ittepic.edu.mx',
    'password': '1145Orbea'
}

response = requests.post(login_endpoint, json=login_payload)
response_data = response.json()
api_token = response_data['id']
print(f'API Token: {api_token}'+ '\n'+"response_data: "+str(response_data))

query_endpoint = f'{metabase_url}/api/card/27/query'
headers = {
    'X-Metabase-Session': api_token
}
#http://localhost:31111/question/27-selectclients
# For a simple GET request. Some queries might require a POST request.
response = requests.post(query_endpoint, headers=headers)
query_result = response.json()

print("query result:"+str(query_result))

# Extract rows and column names
rows = query_result['data']['rows']
column_names = [col['name'] for col in query_result['data']['cols']]

# Write to CSV
with open('metabase_query_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_names)  # Write the header row
    writer.writerows(rows)  # Write the data rows