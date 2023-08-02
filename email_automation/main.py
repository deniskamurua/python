import smtplib
import datetime as dt
import random

MY_EMAIL = "kamuruamuguthi420@gmail.com"
MY_PASSWORD = "fnrsveuzffmvnffs"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="kingpindeno1234@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
