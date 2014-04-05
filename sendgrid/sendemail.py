import sendgrid

sg = sendgrid.SendGridClient('username', 'password') #TODO: fix this after signing up for the site

message = sendgrid.Mail()
message.add_attachment_stream('filename', 'content') #TODO

message.addto('persons email <a@b.com>') #TODO: have them input an email address, then pass that to here
message.set_subject('Your Shopping Liste')
message.set_text('list') #?
message.set_from('our email<b@a.com>') #TODO
status, msg = sg.send(message)
