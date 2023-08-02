import smtplib

email = "kamuruamuguthi420@gmail.com"
password = "fnrsveuzffmvnffs"
to_email = "kingpindeno1234@gmail.com"

# connection = smtplib.SMTP("smtp.gmail.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=to_email, msg="Subject:Greetings\n\nWelcome to the real world")

# connection.close()
