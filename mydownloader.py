import requests

url = input("enter your address")
filename = input("enter file name with file format")
#url = "https://files.virgool.io/upload/users/501/posts/kt6x7pmetr3h/ntsy0szydk5z.jpeg"
data = requests.get(url).content
with open(filename,"wb") as g:
    g.write(data)
