import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

from matplotlib import pyplot as plt
def plt_showRGB(img):
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()

# 全局变量 path 图片路径
path = ''

# 从本地选取图片
def choose_file():
    global path
    path = tk.filedialog.askopenfilename(title='选择文件')  # 选择文件

# 更改图片尺寸
def modImageSize(size):
    width,height = size
    while(width>600 or height>600):
        width=int(width//1.5)
        height=int(height//1.5)
    return width,height

# 更改车牌尺寸（车牌图片）
def modPlateSize(size):
    width,height = size
    while(width>100 or height>100):
        width=int(width//1.5)
        height=int(height//1.5)
    return width,height

# 全局变量 原图
origin_image = 0

# 在窗口展示图片
def showImg(path):
    global origin_image
    load = Image.open(path)
    img = np.array(load)
    origin_image = img
    #plt_showRGB(origin_image)
    height,width,channel = img.shape
    # height = height//2
    # width = width//2
    img_resize = cv2.resize(img,modImageSize((width,height)),interpolation=cv2.INTER_AREA)
    load = Image.fromarray(img_resize)
    render = ImageTk.PhotoImage(load)
    imgLabel = tk.Label(image=render)
    imgLabel.image = render
    imgLabel.place(x=10,y=40)

# 测试全局变量 origin_image 有没有获得值
def test1():
    global origin_image
    if type(origin_image) != type(0):
        plt_showRGB(origin_image)

# 图片处理函数 (图片处理全部写在这里)
def process():
    print('图片处理')

# 创建窗口
top = tk.Tk()
top.title('车牌识别')
top.geometry('900x600')

oriLabel = tk.Label(top,text='原图：')
oriLabel.place(x=10,y=10)

plateLabel = tk.Label(top,text='形状定位车牌位置：')
plateLabel.place(x=620,y=20)
resultLabel = tk.Label(top,text='形状定位车牌位置：')
resultLabel.place(x=620,y=80)
resultLabel = tk.Label(top,text='颜色定位识别结果：')
resultLabel.place(x=620,y=140)

submit_button1 = tk.Button(top, text ="选择文件", command = choose_file)
submit_button1.place(x=620,y=350)
submit_button2 = tk.Button(top, text ="上传原图", command = lambda:showImg(path))
submit_button2.place(x=620,y=400)
submit_button3 = tk.Button(top, text ="识别", command = lambda:test1())
submit_button3.place(x=620,y=450)


top.mainloop()