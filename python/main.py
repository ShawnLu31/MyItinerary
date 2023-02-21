import requests
import api as api
import function as Fc
import keyword as kw


# MY_API_KEY = "AIzaSyAh-z7VrAeBlt_2IGCJWMlSQOUtWndj3pA"
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry"
key = "&key=" + kw.API_KEY
url = url + key

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
