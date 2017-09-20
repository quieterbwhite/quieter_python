# -*- coding=utf-8 -*-
# Created Time: Tue 21 Apr 2015 11:21:29 AM CST
# File Name: barcode.py

'''
生成条形码
'''

from __future__ import absolute_import
from __future__ import unicode_literals

from elaphe import code128
from PIL import Image,ImageDraw,ImageFont


def get_bar_code(bianma, fangweima):
    ''' 根据防伪码和编码生成二维码

        .ttc 是字体文件
        返回条形码图片名
        注意:字体文件，存储图片文件路径的处理, 可以使用常量
    '''

    bc = code128.Code128()
    a = bc.render(fangweima, options=dict(includetext=True), scale=2, margin=1)  # 这里需要填充防伪码

    fnt=ImageFont.truetype('wqy-microhei.ttc', 40)  # 这个字体需要把字体设定好，字体文件目录要对。
    img = Image.new('RGB',(400,240),(255,255,255))
    b = ImageDraw.Draw(img)
    b.text((15,2),'NO:'+bianma,(0,0,0), font=fnt)   # 这里文本填充编码：格式为“No:编码”

    img_w, img_h = img.size
    icon = a
    icon_w, icon_h = icon.size
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2) + 15
    h = int((img_h - icon_h) / 2) + 25
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)

    filename = fangweima + '.png'
    img.save('pics/' + filename)
    return filename


def main():

    bianma = 'ZGYH201500101'
    fangweima = '128135635798'
    get_bar_code(bianma, fangweima)

    print 'Done'


if __name__ == '__main__': main()
