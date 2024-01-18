import smtplib, ssl, time
#from requests import get

level = 2

def send_email_ssl(recipient, email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender = "codefirstburner1@gmail.com"
    password = "wmhtzpiccjtomcgj"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email)
        print('Sent')
        smtp.close()

def send_email(recipient, email, sender, smtp):
    port = 25

#    ip = get('https://api.ipify.org').content.decode('utf8')
#    print('My public IP address is: {}'.format(ip))

    #sender='thesender@dnka.co.za'
    #receiver='julian@finmon.co.za'
    #password=''

    #smtpserver=smtplib.SMTP("smtp.saix.net",587)
    smtpserver=smtplib.SMTP(smtp,port)
    smtpserver.set_debuglevel(level)
    smtpserver.ehlo('smtp.' + sender.split('@')[1])
    #smtpserver.starttls()
    #smtpserver.ehlo
    time.sleep(1)
    #smtpserver.login(sender,password)
    #msg='Subject:Demo\nThis is a demo'
    #smtpserver.sendmail(sender,receiver,msg)
    smtpserver.sendmail(sender, recipient, email)
    print('Sent')
    smtpserver.close()
    return(1)

if __name__ == '__main__':
    import sys
    sys.exit(send_email("<your-user>@<your-email.domain>","Subject: Hi there!\n\nHowzit!\n","fjhgqtaa@sharklasers.com"))
