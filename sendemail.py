import smtplib
import email.message

from_addr = ' '

to_addr = ' '

m = email.message.Message()
m['From'] = "  "
m['To'] = "  "
m['Subject'] = "Send mail from python!!"

m.set_payload("Another test.... tell me if you get that email");

message_to_send= m.as_string()


# Credentials (if needed)
username = ' '
password = '  '

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()