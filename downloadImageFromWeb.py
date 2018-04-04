import random
import urllib.request

def download(url):
    name=random.randrange(1,25)
    full_name= str(name)+".jpeg"
    urllib.request.urlretrieve(url,full_name)

download("http://img.huffingtonpost.com/asset/,scalefit_950_800_noupscale/55fc14631c00004800082775.jpeg")