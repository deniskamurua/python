import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

email = "kamuruamuguthi420@gmail.com"
password = "fnrsveuzffmvnffs"
to_email = "kingpindeno1234@gmail.com"

header = headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                           "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}


response = requests.get("https://www.amazon.com/Dell-Optiplex-9020-DisplayPort-Bluetooth/dp/B08BJDFZRF?ref_"
                        "=Oct_d_oup_d_565098_0&pd_rd_w=hxNOl&content-id=amzn1.sym.4d915fa8-ca05-4073-b385"
                        "-a93e1e1dd22d&pf_rd_p=4d915fa8-ca05-4073-b385-a93e1e1dd22d&pf_rd_r=14S4PDXYJFQ0EC0M565H"
                        "&pd_rd_wg=xDgGR&pd_rd_r=a5a9e094-a969-4a36-8fd8-a882f1804ede&pd_rd_i=B08BJDFZRF&th=1",
                        headers=header)
soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
if price_as_float < 100:
    with smtplib.SMTP("smtp.gmail.com") as c:
        c.starttls()
        c.login(user=email, password=password)
        c.sendmail(from_addr=email, to_addrs=to_email, msg="Subject:Reasonable price\n\nPrice is blow 100$. visit:"
                                                       "https://www.amazon.com/Dell-Optiplex-9020-DisplayPort"
                                                       "-Bluetooth/dp/B08BJDFZRF?ref_"
                                                       "=Oct_d_oup_d_565098_0&pd_rd_w=hxNOl&content-id=amzn1.sym"
                                                       ".4d915fa8-ca05-4073-b385"
                                                       "-a93e1e1dd22d&pf_rd_p=4d915fa8-ca05-4073-b385-a93e1e1dd22d"
                                                       "&pf_rd_r=14S4PDXYJFQ0EC0M565H"
                                                       "&pd_rd_wg=xDgGR&pd_rd_r=a5a9e094-a969-4a36-8fd8-a882f1804ede"
                                                       "&pd_rd_i=B08BJDFZRF&th=1"
               )
