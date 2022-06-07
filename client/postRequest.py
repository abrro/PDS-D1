import http.client
import json

#Address = IP given to LoadBalancer service in kubernetes
#Port = LoadBalancer's port
conn = http.client.HTTPConnection("127.0.0.1", 8088)
payload = json.dumps({
  "ime": "Andrej",
  "prezime": "Brocic",
  "username": "abrocic13318ri",
  "smer": "RI",
  "predmeti": [
    {
      "ime": "PDS",
      "espb": 6
    },
    {
      "ime": "NRS",
      "espb": 6
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))