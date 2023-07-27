import requests
import time

def time_to_load(link):
    time_before = time.time()
    get = requests.get(link)
    time_after = time.time()
    print(f"It took {time_after - time_before} seconds to load a {link} page.")


time_to_load("https://www.google.com")
time_to_load("https://www.imdb.com")
time_to_load("https://www.ynet.co.il/home/0,7340,L-8,00.html")