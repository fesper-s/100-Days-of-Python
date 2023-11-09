import smtplib, datetime, random

MY_EMAIL = "fabricio_esper@outlook.com"
MY_PASSWORD = "password123"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as fd:
        all_quotes = fd.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )