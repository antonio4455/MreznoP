
import smtplib 
import email.utils

content = 'test message' 

content = smtplib.SMTP('smtp.gmail.com', 587)

email.ehlo()
email.starttls()
email.login('email', 'password')

email.sendmail('test@gmail.com', 'anteprojic@gmail.com', content)

email.close()