import sendgrid

sg = sendgrid.SendGridClient('username', 'password') #TODO: fix this after signing up for the site

message = sendgrid.Mail()

message.addto('persons email <a@b.com>') #TODO: have them input an email address, then pass that to here
message.set_subject('Your Shopping List, from Liste!')
message.set_text('list') #?
message.set_from('our email<b@a.com>') #TODO
status, msg = sg.send(message)

#have a flask route, send email. pass in one parameter, the email you want to send to, put this code in the flask route
#do a database query to grab the text. render_template method in flask. 
#use bitcamp as the website