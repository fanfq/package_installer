from tkinter import *

window = Tk()   # 创建应用窗口
window.title('Entry demo')     # 窗口设置标题
window.geometry('300x300+200+200')  # 设置窗口大小与位置，widthxheight+left+top，宽高之间的是小写字母 x

# 按钮事件，获取输入框的值
def get_entry_value():
    print(entry.get())
    entry_value.set("获取输入框的值：%s" % entry.get())

# 定义输入框值的变量
entry_value = StringVar()

# 创建输入框
entry = Entry(window, width=10)
entry.place(x=0, y=0)

# 创建按钮
btn = Button(window, text="获取输入框的值", command=get_entry_value)
btn.place(x=100, y=0)

# 创建标签
label = Label(window, textvariable=entry_value)
label.place(x=0, y=30)

window.mainloop()