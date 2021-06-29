from python_graphql_client import GraphqlClient
import requests

# Instantiate the client with an endpoint.
# client = GraphqlClient(endpoint="https://anilist.co/graphiql")

# Create the query string and variables required for the request.
query = """
    query {
        media {
            id,
            startDate
        }
    }
"""
# variables = {"countryCode": "CA"}

# Synchronous request
# data = client.execute(query=query)
response = requests.post(url="https://anilist.co/graphiql")
print(response.text)
# print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}
