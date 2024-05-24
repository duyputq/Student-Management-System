import smtplib
import getpass
#Set up email
email='duy20nguyen04@gmail.com'
# password=getpass.getpass('Pass: ')
password='rwlg omeh okun vdvd'
email_sent='21021571@vnu.edu.vn'
#Doc tep email
fi=open('gmail.txt', encoding='utf8')
email_sent=[]
r=fi.read().split();
email_sent.append(r);

#xuly
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls() #enable security
session.login(email,password)
#noidung
mail_content='''Subject: Thong bao ve hoc bong lan hai
Dai hoc Cong nghe tran trong thong bao:

Chuc mung ban da duoc hoc bong!!

Keep trying! 
'''
for _ in range(len(email_sent)):
    session.sendmail(email,email_sent[_],mail_content)

print('Your mail has been sent!')
