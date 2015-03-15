import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail():
    img_data = open('fire.jpg', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Fire'
    msg['From'] = 'cvfiredetector'
    msg['To'] = 'parthibhank82@gmail.com'
    
    frm = 'cvfiredetector@gmail.com'
    toaddr = 'parthibhank82@gmail.com'

    text = MIMEText("FIRE DETECTED !!!!!!!!!")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('fire.jpg'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user = 'cvfiredetector@gmail.com', password = 'nirmalraj')
    s.sendmail(frm, toaddr, msg.as_string())
    s.quit()
