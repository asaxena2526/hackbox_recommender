import http.client

conn = http.client.HTTPSConnection("ott-details.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "ott-details.p.rapidapi.com",
    'x-rapidapi-key': "key to be added as previous one expired"
    }

conn.request("GET", "/search?title=Endgame&page=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
