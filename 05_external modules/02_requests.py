import requests
r = requests.get('https://api.github.com/users/aasthak-collab')
with open("aasthak-collab.txt", "w") as f:
    f.write(r.text)