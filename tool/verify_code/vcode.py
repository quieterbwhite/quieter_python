# -*- coding=utf-8 -*-
# Created Time: 2016年08月04日 星期四 11时12分45秒

"""
生成图片验证码

这段代码我在网上找的，历经我待过的3个公司，知数科技，理想境界，云和科技

这段代码是完全可以单独使用的

pip install Pillow
"""

import time
import random
import hashlib
import datetime

from PIL import Image, ImageDraw, ImageFont, ImageFilter

from logs.mylog import flogger

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

_letter_cases = "abcdefghjkmnpqrstuvwxy"
_upper_cases  = "ABCDEFGHJKLMNPQRSTUVWXY"
_numbers      = "1234567890"
init_chars    = "".join((_letter_cases, _upper_cases, _numbers))

class ImageVerifyService(object):
    """
    @param key: 和验证码对应的唯一值（例如手机号）
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param chars: 允许的字符集合，格式字符串
    @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_size: 验证码字体大小
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param length: 验证码字符个数
    @param draw_lines: 是否划干扰线
    @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
    @param draw_points: 是否画干扰点
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: PIL Image实例
    @return: [1]: 验证码图片中的字符串
    """

    def generate_verify_image(self,
                             size=(120, 30),
                             chars=init_chars,
                             img_type="GIF",
                             mode="RGB",
                             bg_color=(253, 203, 176),
                             fg_color=(171, 72, 7),
                             font_size=18,
                             font_type="DejaVuSans.ttf",
                             length=4,
                             draw_lines=True,
                             n_line=(1, 2),
                             draw_points=True,
                             point_chance=2):
        width, height = size # 宽， 高
        img = Image.new(mode, size, bg_color) # 创建图形
        draw = ImageDraw.Draw(img) # 创建画笔

        def get_chars():
            """生成给定长度的字符串，返回列表格式"""
            return random.sample(chars, length)

        def create_lines():
            """绘制干扰线"""
            line_num = random.randint(*n_line) # 干扰线条数

            for i in range(line_num):
                # 起始点
                begin = (random.randint(0, size[0]), random.randint(0, size[1]))
                # 结束点
                end = (random.randint(0, size[0]), random.randint(0, size[1]))
                draw.line([begin, end], fill=(0, 0, 0))

        def create_points():
            """绘制干扰点"""
            chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]

            for w in xrange(width):
                for h in xrange(height):
                    tmp = random.randint(0, 100)
                    if tmp > 100 - chance:
                        draw.point((w, h), fill=(0, 0, 0))

        def create_strs():
            """绘制验证码字符"""
            c_chars = get_chars()
            strs = " %s " % " ".join(c_chars) # 每个字符前后以空格隔开

            font = ImageFont.truetype(font_type, font_size)
            font_width, font_height = font.getsize(strs)

            draw.text(((width - font_width) / 3, (height - font_height) / 3),
                        strs, font=font, fill=fg_color)

            return "".join(c_chars)

        if draw_lines:
            create_lines()
        if draw_points:
            create_points()

        strs = create_strs()

        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]

        img = img.transform(size, Image.PERSPECTIVE, params) # 创建扭曲

        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）

        mstream = StringIO.StringIO()

        img.save(mstream, img_type)

        # 保存图片到文件
        #img.save("validate.gif", img_type)

        stream = mstream.getvalue().encode("base64")

        return strs, stream

def md5(key):
    m = hashlib.md5()
    m.update(key)
    return m.hexdigest()

def generate_key():
    """ 生成唯一的key """

    return md5(str(time.time())+str(random.randint(1000, 9999)))

def gen_verify_code():

    key = generate_key()
    image_service = ImageVerifyService()

    try:
        strs, stream = image_service.generate_verify_image()
    except Exception as e:
        flogger.exception(e)
        return None

    data = {
        "key"  : key,
        "pic"  : stream,
        "code" : strs
    }

    return data

def main():

    data = gen_verify_code()


if __name__ == "__main__":
    main()

