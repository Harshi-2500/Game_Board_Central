import http.client
import urllib.parse
import json

server_host = 'localhost'

try: 
    conn=http.client.HTTPConnection(server_host, 13000)
    req_data = {'message': 'Hello'}

    url = "/message_passing?"+urllib.parse.urlencode(req_data)
    conn.request('GET', url)
    response = conn.getresponse()

    if response.status == 200:
        response_content = json.loads(response.read().decode('utf-8'))
        print(response_content)

    else:
        print("Response not recieved")

except Exception as e:
    print(f"Error message:{e}")