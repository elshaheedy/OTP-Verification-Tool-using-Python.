import random
import smtplib
from tkinter import *

# generate 6-digit OTP
OTP = random.randint(100000, 999999)

# send email function
def send_email():
    # create SMTP session
    email = email_entry.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # login to sender email account
    sender_email = "m.alshahedy12@gmail.com"
    sender_password = "cdqsjyqubjirwegc"
    server.login(sender_email, sender_password)

    # message to be sent
    global OTP
    OTP = random.randint(100000, 999999)
    message = f'Your OTP is {OTP}.'

    # send email
    server.sendmail(sender_email, email, message)
    print('OTP sent successfully!')
    server.quit()

# verify OTP 
def verify_otp():
    entered_otp = otp_entry.get()
    if int(entered_otp) == OTP:
        print('OTP verification successful!')
    else:
        print('OTP verification failed!')

    
# create GUI
window = Tk()
window.title('OTP Verification')

# create labels
Label(window, text='Enter your email:').grid(row=0, column=0)
Label(window, text='Enter the OTP:').grid(row=1, column=0)

# create entries
email_entry = Entry(window)
otp_entry = Entry(window)

# grid entries
email_entry.grid(row=0, column=1)
otp_entry.grid(row=1, column=1)

# create buttons
send_otp_button = Button(window, text='Send OTP', command=send_email)
verify_otp_button = Button(window, text='Verify OTP', command=verify_otp)

# grid buttons
send_otp_button.grid(row=2, column=0)
verify_otp_button.grid(row=2, column=1)

window.mainloop()
