from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import prettytable as pt
to = input("收件人:")
subject = input("邮件主题:")
print("选择邮件附件:")

'''
#python窗口类型,拾色器,文件选择,文件打开
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *

import tkinter.filedialog
f=askcolor(color=None, title='颜色选取')  
print (f)

f = askopenfilename(title='askopenfilename', initialdir="D:", filetypes=[('所有文件', '*.*'), ('Python源文件', '.py')])
#f1 = asksaveasfilename(title='asksaveasfilename', initialdir="E:", filetypes=[('所有文件', '*.*'), ('Python源文件', '.py')])

'''
'''
def xz():
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您选择的文件是'+filename)
    else:
         lb.config(text='您没有选择任何文件')

root = Tk()

lb = Label(root,text='')
lb.pack()
btn=Button(root,text='选择要发送的附件文件',command=xz)
btn.pack()
root.mainloop()
'''

'''
##打印表格
import prettytable as pt
'''
'''
+--------------------+----------+---------------------------+
|     收件人地址     | 邮件主题 |          附件名称         |
+--------------------+----------+---------------------------+
| ************ |  winxp   | D:/pythonApp/tkwindows.py |
+--------------------+----------+---------------------------+
'''
'''
# tb = pt.PrettyTable( ["City name", "Area", "Population", "Annual Rainfall"])
tb = pt.PrettyTable()
tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tb.add_row(["Adelaide",1295, 1158259, 600.5])
tb.add_row(["Brifasdfae",5905, 1857594, 1146.4])
tb.add_row(["Darwin", 112, 120900, 171423423423423424.7])
tb.add_row(["Hobart", 1357, 205556,619.5])

print(tb)
'''
'''
root = Tk()
#root.geometry('600x500')
msg1 = Message(root,text=tb,relief=GROOVE)
msg1.place(relx=0.2,rely=0.4,relheight=0.4,relwidth=0.5)
root.mainloop()
'''
filename = tkinter.filedialog.askopenfilename()
tb = pt.PrettyTable()
tb.field_names = ["收件人地址", "邮件主题", "附件名称"]
tb.add_row([to, subject, filename])
print(tb)
