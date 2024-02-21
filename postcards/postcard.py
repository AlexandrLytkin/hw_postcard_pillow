import os

from PIL import Image, ImageFont, ImageDraw, ImageColor


class PostCardMaker:
    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = template
        if font_path is None:
            self.font_path = "/Users/aleksandrlytkin/PycharmProjects/hw_postcard_pillow/fonts/ofont.ru_DS Eraser2.ttf"
        else:
            self.font_path = font_path

    def make(self):
        im = Image.open("postcard.jpg")
        w, h = im.size
        resize_image = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(resize_image)
        font = ImageFont.truetype(self.font_path, size=40)

        y = resize_image.size[1] - 20 - font.size
        message = f'Hello, {self.name}'
        # draw.text((100, 10), "Hello", font=font, fill='#ff0000')
        draw.text((125, y), message, font=font, fill=ImageColor.colormap['coral'])

        # resize_image.save("change_postcard.jpg")
        resize_image.show()


if __name__ == '__main__':
    maker = PostCardMaker('Aleksandr')
    maker.make()
