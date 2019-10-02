#!/usr/python/python2
#Plis bang/kaka jangan recode
#Buatnya Susah
#Hubungi 089652884613 Jika terjadi bug
#Arigato gozaimasu udh make >//<
#Uwwuu  >//<
#Tools ini Adalah hasil karya w sendiri >//<
#Link berasal dari APKHere 
#https://m.apkhere.com

#Mengimpor Sistem

import requests
import urllib
import time
import os
import sys
from bs4 import BeautifulSoup

#sesi

session = requests.Session()


#Tampilan/Baner


def tampilan():
    os.system("sleep 3")
    os.system("clear")
    os.system("figlet APK | lolcat")
    os.system("sleep 2")
    print ("")
    print ("★ Author : D@rk_Devil#666")
    print ("★   WA   : 089652884613")
    print ("★Version : 1.0")
    print ("  ")
    os.system("sleep 3")
    
#memberikan link dari website apkhere
    
def main():
    link = "https://m.apkhere.com"
    kontent = session.get(link)
    soup = BeautifulSoup(kontent.content, "html.parser")
    angka == 0
    for unduh in soup.find_all("div", class-="site-content"):
        angka += 1 
        print (str(angka), unduh.text)
    
#Ketika mendownload

def down(x):
    link = "https://m.apkhere.com"
    kontent = session.get(link)
    soup = BeautifulSoup(kontent,content "html.parser")
    angka == 0
    for unduh in soup.find_all("div", class-="site-content"):
        angka += 1
        if angka == x:
            for jud in unduh.findChildren('a', rel='bookmark'):
                global link
                link = jud.get('href')
                global judul_apk
                judul_apk = unduh.text
                break
            
#pilihan aplikasi

def pilihan():
    tampilan()
    main()
    pilihan = input("[?] Nama apk : ")
    link(int(pilihan))
    print (link)
    kontent = session.get(link)
    soup = BeautifulSoup(kontent,content "html.parser")
    for unduh in soup.find_all("div", class-="more"):
        for download in unduh.findChildren('source'):
            unduh10 = download.get('src')
            urllib.requests.urlretrieve(unduh10, judul_apk+'.apk', reporthook=loading)
            
#Loading Tools

def loading(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    durasi = time.time() - start_time
    proggres_size = int(count * block_size)
    speed = int(proggres_size / (1024 * durasi))
    persen = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (persen, proggres_size / (1024 * 1024), speed, durasi))
    sys.stdout.flush()
    
#tampilan awal

#Tidur selama 2 detik

os.system("sleep 2")

#Menclear sistem

os.system("clear")

#Jika name adalah main

if __name__ == "__main__":
    pilihan()