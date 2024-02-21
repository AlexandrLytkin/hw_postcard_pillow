from PIL import Image, ImageFont, ImageDraw, ImageColor
class PostCardMaker:
    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = template
        if font_path is None:
            self.font_path = "/Users/aleksandrlytkin/PycharmProjects/hw_postcard_pillow/fonts/ofont.ru_DS Eraser2.ttf"
        else:
            self.font_path = font_path
    def make(self, resize=False, out_path=None):
        im = Image.open("postcard.jpg")
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=30)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f'Привет, {self.name}'
        # draw.text((100, 10), "Hello", font=font, fill='#ff0000')
        draw.text((125, y), message, font=font, fill=ImageColor.colormap['coral'])

        y = im.size[1] - 20 - font.size
        message = f'с праздником тебя'
        # draw.text((100, 10), "Hello", font=font, fill='#ff0000')
        draw.text((125, y), message, font=font, fill=ImageColor.colormap['coral'])
        # im.show()
        out_path = out_path if out_path else 'post_card.jpg'
        im.save(out_path)
        print(f'Post card saved as {out_path}')
if __name__ == '__main__':
    maker = PostCardMaker('Aleksandr')
    maker.make()
