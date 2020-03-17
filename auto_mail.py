import yagmail


from_email = "yourmail@gmail.com"
password = "yourpassword"
to_email = "i_numn@yahoo.com"  # receiver email address
subject = "Attendance Report"
body = "Attendence File"  # email body
fileName="Attendance\Attendance_2020-03-02_15-28-25.csv" # attach the file

# mail information
yag = yagmail.SMTP(from_email, password)

# sent the mail
yag.send(
    to = to_email,
    subject = subject,  # email subject
    contents = body,  # email body
    attachments = fileName,  # file attached
)


# https://myaccount.google.com/lesssecureapps we'll have to allow less secure app 

#  and if there's any 2-step verification turn it off else it'll not send mail