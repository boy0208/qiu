from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os
import platform
import uuid


class VerificationCode(object,):
    '''用于生成随机验证码'''

    def __init__(self,file_name):
        self.str_code = list(range(65, 91))
        self.str_code += list(range(97, 123))
        self.str_code += list(range(48, 58))
        self.file_name = file_name + '.png'

    #  生成随机字符 a~z, A~z, 0~9
    def random_str(self):
        return chr(random.choice(self.str_code))

    # 生成随机颜色:
    def random_color(self):
        return random.randint(0, 245), random.randint(0, 245), random.randint(0, 245)

    # 生成验证码和图片
    def generate_code(self):
        # 240 x 60:
        width = 60 * 4
        height = 60
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 根据操作系统获取字体文件
        if platform.uname().system == 'Windows':
            ttf = 'arial.ttf'
        elif platform.uname().system == 'Linux':
            ttf = '/usr/share/fonts/arial/ARIAL.TTF'
        font = ImageFont.truetype(ttf, 50)
        draw = ImageDraw.Draw(image)
        # 随机生成两条直线（一条贯穿上半部，一条贯穿下半部）
        draw.line((0, 0 + random.randint(0, height // 2),
                   width, 0 + random.randint(0, height // 2)),
                  fill=self.random_color())
        draw.line((0, height - random.randint(0, height // 2),
                   width, height - random.randint(0, height // 2)),
                  fill=self.random_color())
        # 输出文字
        code_str = ''
        for t in range(4):
            tmp = self.random_str()
            # print(tmp, ord(tmp))
            draw.text((60 * t + 10, 10), tmp, font=font, fill=self.random_color())
            code_str += tmp
        # 模糊处理
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # print(image)
        # # 图片保存
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # path_name = os.path.join(base_dir, './', self.file_name)
        # image.save(path_name, 'png')
        # with open(path_name,"rb") as f:
        #     print(f)
        #     a  = f.read()
        #     print(a)
        return code_str, image


if __name__ == '__main__':
    ver_code = VerificationCode('验证码')
    code = ver_code.generate_code()
    print(code)
