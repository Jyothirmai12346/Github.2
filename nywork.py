import requests
url= "https://api.github.com/orgs/microsoft/repos"
response=requests.get(url)
repos=response.json()
print(" Microsoft open source repositories")
for repo in repos[5]:
  Name=repo["Name"]
  Description=repo["Description"]
  Url=repo["Url"]
  print("Repository name :",Name)
  print("Description:",Description)
  print("url:",Url)
