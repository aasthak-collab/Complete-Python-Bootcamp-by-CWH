#request module is used to fetch any website's html code 
import requests
r = requests.get("https://www.perplexity.ai/")
print(r.text)