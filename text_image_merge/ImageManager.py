from PIL import Image
import random


class ImageManager:
    def __init__(self, fonts: list = [],
                 img_path: str = '', img: Image = None,
                 text: str = ''):
        self.fonts: list = []
        self.font: str = ''
        self.main_img: Image
        self.text: str = text

        if img_path:
            self.main_img = Image.open(img_path)
        elif img:
            self.main_img = img
        else:
            print("Warning : there's no img in here.")
            self.main_img = Image.open("")

        # default setting
        self.settings = {
            'random font': True,
            'square img': True,
            'text in middle': True,
            'text vertical': False,
        }

        if fonts:
            self.set_fonts(fonts)

    # region edit and add image

    def resize_image(self, size: tuple = (1024, 1024)):
        # add some features..
        img_size = self.main_img.size

        if self.settings['square img'] and img_size[0] == img_size[1]:
            self.main_img.resize(size)
            return

        if img_size[0] * size[1] > img_size[1] * size[0]:
            # if there is extra length size
            length = int(size[0] * (img_size[1]/size[1]))
            diff = int(img_size[0] - length) // 2
            self.main_img = self.main_img.crop((diff, 0, length + diff, img_size[1]))
        else:
            # if there is extra width size
            width = int(size[1] * (img_size[0]/size[0]))
            diff = int(img_size[1] - width) // 2
            self.main_img = self.main_img.crop((0, diff, img_size[0], width + diff))

        self.main_img = self.main_img.resize(size)
        return

    def open_image(self, img_path: str) -> None:
        self.main_img = Image.open(img_path)

    # endregion

    # region font and font size

    def set_font(self, font_path: str) -> None:
        self.fonts.append(font_path)

    def set_fonts(self, fonts: list) -> None:
        for font_path in fonts:
            self.set_font(font_path)

    def set_font_size(self) -> int:
        if self.main_img is None:
            print("Warning : there's no img in here.")
            return 1

        img_size = self.main_img.size
        # editing
        return 10

    # endregion


