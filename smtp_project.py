

# # Send message with email
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("eaxample@gmail.com","password")
server.sendmail('example@gmail.com',
                "kinggmail.com",
                "hello rayyan ,how are u ?")
server.quit()