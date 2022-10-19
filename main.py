#!usr/bin/python

import imaplib
from logging import root
import time

from tkinter import *

imap_host = 'imap.gmail.com'
imap_user = 'dallin@yauney.net'
imap_pass = 'srghmjrqbjaozrxv'


tkbg = "Light Blue"

window = Tk()
window.title("This is the title")
window.geometry("650x600")
window.config(background = tkbg)

main_content = Text(window) 



# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Testing')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')

	# print('Message: {0}\n'.format(num))
	# print(data[0][1])

    main_content.insert(INSERT, data)

    # break
imap.close()





main_content.pack()

window.mainloop()