from PIL import Image
from urllib.request import urlopen

btc_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
eth_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
link_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png'))
dot_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png'))
ada_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png'))

header_image = Image.open(urlopen('https://images.ctfassets.net/0idwgenf7ije/6OUAGu0C76BTCRaJ9t9rs7/9bcfc6d0ae3c0247a2d1b87157f964a3/Gemini-Non-Fungible_Token-_One_of_a_Kind_Assets_for_Collectibles_and_Rare_Items.png?fm=webp'))
blockchain_image = Image.open(urlopen('https://www.industry.gov.au/sites/default/files/December%202019/image/the-national-blockchain-roadmap-figure-2.png'))
crypto_image = Image.open(urlopen('https://d1xple9gxb4tux.cloudfront.net/assets/images/article_images/88778f25986d1f7826e6f4f6ff2a664c92958083.png?1554975116'))
crypto_image_2 = Image.open(urlopen('https://s3.cointelegraph.com/storage/uploads/view/7c1346d1f2019b433701e8f6b9b3a8b3.png'))