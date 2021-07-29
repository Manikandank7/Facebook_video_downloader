import re
import requests
import progressbar
import urllib.request
from time import sleep

class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()

link=input("vdeo_url:")
filename=input("file_name:")


while True:
    try:
        html=requests.get(link)
        try:
            url=re.search('hd_src:"(.+?)"',html.text)[1]
            print("HD")
        except:
            url=re.search('sd_src:"(.+?)"',html.text)[1]
            print("SD")
        print("downloading . . .")
        urllib.request.urlretrieve(url,filename+".mp4",MyProgressBar())
        print("download successful")
        break
    except Exception as e:
        print(e)
        print("Retrying . . .")
        sleep(3)
