import pyqrcode
import png
from pyqrcode import QRCode

#taking the name of the png from the user 
png_name = input("enter the name of the qrcode :")

#generating the name of the png file
png_file = png_name+".png"

#taking the link from the user
code = input("give a link :")

#genereting the qrcode 
url = pyqrcode.create(code)

#creating the png of the qrcode
url.png(png_file,scale=6)
