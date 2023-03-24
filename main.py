

import tweepy
import time
import fitz
from PIL import Image
import aladhan
from datetime import datetime
import pytz


print("start")

a = "njf0n2KymdoL2F41YYSqjGvPa"
b = "dCYH8x6CUiNnwVlWARJNY6q8hMvIkZUucb8YNRgbix1tj35RSl"
c = "1538214226828972034-7cEi1nXDRJm1ygPOoGazG3TpKtJZ6F"
d = "Hx1OJr8El7UdXDuevs34GDIBGcK45HPqoFjx7AfRU7W7c"

authq = tweepy.OAuthHandler(a, b)
authq.set_access_token(c, d)
quranbot = tweepy.API(authq, wait_on_rate_limit=True) 



def QuranPage(n, doc):
 t = 1
 media_ids = []
 print("Allah Akbar")
 
 while t <= 4:
  filename = f"./quranpages/quran({t}).png"
  page = doc.load_page(n)
  pix = page.get_pixmap()
  img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
  img.save(filename, "png")

  res = quranbot.media_upload(filename)
  media_ids.append(res.media_id)
  n += 1 
  t += 1
 
 quranbot.update_status(status=" ", media_ids = media_ids)


 print("page has been downloaded !") 
 return n

def timing(pagesNO, doc):
 
 
   location = aladhan.City("Riyadh", "SA")
   client = aladhan.Client(location)
   times = client.get_today_times()
   dt = datetime.now(pytz.timezone("Asia/Riyadh"))
   currentTime = dt.strftime("{0:%Y/%m/%d} {0:%I:%M (%p)}").format(dt)
   
  
 
   for t in times:
    finaltimeSalah = str(t.readable_timing())
    if finaltimeSalah == str(currentTime):
      print("yeah")
      pagesNO = QuranPage(pagesNO, doc)

  
   
  
   print(pagesNO)
   print(currentTime, finaltimeSalah)
   return pagesNO

doc = fitz.open(r"./quranPDF.pdf")

pagesNO = 1
n = 1
while(True):

  print(n)

  pagesNO = timing(pagesNO, doc)
  time.sleep(60)
  n += 1

  







   
 
   
 
   

