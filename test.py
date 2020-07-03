import cv2
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

def plt_showRGB(img):
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()

# plt显示灰度图片
def plt_showGray(img,*title):
    if len(title)==1:
        plt.title(title[0],fontsize='14',fontweight='bold',color='red')
    plt.imshow(img,cmap='gray')
    plt.show()

i = 0
print(type(i) == type('asdad'))
# 读取图像
image = Image.open("./image/test1.png")
original = np.array(image)
i = original
plt_showRGB(i)
