import tkinter
import tkinter.filedialog
top = tkinter.Tk()
top.title = 'new'
top.geometry('640x480')



def choose_fiel():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
    e.set(selectFileName)



e = tkinter.StringVar()
e_entry = tkinter.Entry(top, width=68, textvariable=e)
e_entry.pack()

path = ''
def upload_func(a):
    global path
    '''
    要自己写个方法，ftp等方法，上传文件到服务器

    '''
    path = a
    print('路径为：',a)
    pass


submit_button = tkinter.Button(top, text ="选择文件", command = choose_fiel)
submit_button.pack()
submit_button = tkinter.Button(top, text ="上传", command = lambda:upload_func(e_entry.get()))
submit_button.pack()

from PIL import Image, ImageTk
def showImg(img1):
    load = Image.open(img1)
    render = ImageTk.PhotoImage(load)

    img = tkinter.Label(image=render)
    img.image = render
    img.place(x=200, y=100)

submit_button = tkinter.Button(top, text ="显示图片", command = lambda :showImg(showImg(path)))
submit_button.pack()



top.mainloop()