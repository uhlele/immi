import smtplib




def send_email(receiver, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()


    gmail_user = 'ishankydv1@gmail.com'  
    gmail_password = 'localhost123'

    sent_from = gmail_user  
    to = [receiver]  
    subject = 'Confirm Email'
    body = body

    email_text = """ 
    Subject: {}


    {}
    """.format(subject, body)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:  
        print ('Something went wrong...')
