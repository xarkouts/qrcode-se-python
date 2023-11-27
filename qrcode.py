import pyqrcode
import png
from pyqrcode import QRCode
from urllib.parse import urlparse
def einai_url(url):
    https="https://"
    if https in url:
        pass
    else:    
     url=https+url
    print(url)
    try:
     apotelesma=urlparse(url)
     return all([apotelesma.scheme,apotelesma.netloc])
    except ValueError:
        return False   
        
    
while (True):
 url=input("Δοσε το url  \n")
 if einai_url(url)==True:
     break
 else:
     print("Αυτο που πρικτρολογισες δεν ειναι url")
     continue
qrc=pyqrcode.create(url)
qrc.png("qrcode.png",scale=7)
print("To qrdoce δημιουργιθηκε με")