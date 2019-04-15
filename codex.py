#d3xt3r0

'''
This is a text editor that has gone mad.

'''
import os.path
import Tkinter as tk

def onKeyPress(event):
    first=event.char
    second=ord(first)
    a=[97,99,101,103,105,107,109,111,113,115,117,119,121]
    i=0
    while i<(len(a)):
            if (second==a[i]):
                if (i<=12):
                     second=chr(a[i+1])
                     text.insert('end', '%s' % (second ))
                     f.write(first)
            elif (second==121):
                     second=chr(97)
                     text.insert('end', '%s' % (second ))
                     f.write(first)
            i=i+1
    if second==32:
        second=chr(second)
        text.insert('end', '%s' % (second ))
    elif second==8:
        length = len(text.get(1.0, 'end'))
        contents = text.get(1.0, 'end')
        newcon = contents[:-2]
        #text.insert('end', '%s' % (length ))
        text.delete(1.0,'end')
        text.insert('end', '%s' % (newcon ))
   
    elif(second>=65 and second<=90 or second>=97 and second<=122):    
        text.insert('end', '%s' % (chr(second) ))
        f.write(first)


def no_op(self):
    return "break"

def infiloop(self):
    while(1):
          continue

root = tk.Tk()
root.config(cursor='none')
root.attributes("-fullscreen", True) 
text = tk.Text(root, background='black', foreground='orange', font=("Comic Sans MS",20))
text.pack(expand=True,)

text.bind("<Tab>", infiloop)
text.bind("<Button-1>", no_op)
text.config(cursor="none")
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
