import pyqrcode

qrcode = pyqrcode.create(content="test",error='H')

qrcode.png(file='test.png',scale=6)
