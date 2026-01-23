import qrcode
from qrcode.image.svg import SvgImage

url = "https://www.instagram.com/river_garage20"

img = qrcode.make(
    url,
    image_factory=SvgImage,
    box_size=20,
    border=2
)

img.save("river_garage_qr.svg")