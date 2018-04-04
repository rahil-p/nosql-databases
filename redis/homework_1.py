from urllib.request import urlopen
import re

url = 'https://api.nasa.gov/planetary/apod?api_key=WxvIyjioREFtUSMXVZXMxugCZsMT3Y33UsXK7ImM&date=1995-07-06'
page = urlopen(url).read().decode('utf-8')

x = re.search("\"url\": \"https://apod.nasa.gov/apod/image/.+?\"",page)
image_url = x.group(0)[8:-1]

print(image_url)