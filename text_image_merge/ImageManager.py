"""

"""
from PIL import Image, ImageDraw, ImageFont
import random
import itertools


class ImageManager:
    """Edit and Add some effect in Image
    """

    # region class FontManager
    class FontManager:
        def __init__(self, fonts: list):
            # elements
            self.paths: dict[str: list] = {}
            self.path: str = ''
            self.size: int = 100

            if fonts:
                self.add_fonts(fonts)

        def add_font(self, font_path: str, ignore_overlap: bool = True, tag: str = "None") -> None:
            """
            add font path in font_paths list
            notice : the path is overlap when the tag is same.

            :param font_path: path that you want to add in font list
            :param ignore_overlap: do not add when font path is already in list(default : True)
            :param tag: add tag in path (default : None)
            :return: None
            """
            if tag not in self.paths.keys():
                self.paths[tag] = []
            if not ignore_overlap or font_path not in self.paths:
                self.paths[tag].append(font_path)

        def add_fonts(self, fonts: list, ignore_overlap: bool = True, tag: str = "None") -> None:
            """
            add font list in font_paths list
            notice : the path is overlap when the tag is same.

            :param fonts: path list that you want to add in font list
            :param ignore_overlap: do not add when font path is already in list(default : True)
            :param tag: add tag in path (default : None)
            :return: None
            """
            for font_path in fonts:
                self.add_font(font_path, ignore_overlap=ignore_overlap, tag=tag)

        def add_fonts_dict(self, fonts: dict, ignore_overlap: bool = True) -> None:
            """
            add font dict in font_path list
            notice : the path is overlap when the tag is same.

            :param fonts: path dict that you want to add in font list
            :param ignore_overlap: do not add when font path is already in list(default : True)
            :return: None
            """
            for font_path, tag in fonts.items():
                self.add_font(font_path, ignore_overlap=ignore_overlap, tag=tag)

        def set_font_random(self, tags=None) -> None:
            """
            set font random in font list

            :param tags: if you want to pick random in particular tag, write it (str or list)
            :return: None
            """
            if type(tags) is str:
                tags = [tags]

            path_list: list = []
            if type(tags) is list:
                path_list = list(itertools.chain(
                    *[self.paths[temp_tag] for temp_tag in tags
                      if temp_tag in self.paths.keys()]))
                if len(path_list) == 0:
                    print(f"!warning : the tag list {tags} does not exist in path dict. pick random.")
                    path_list = list(itertools.chain(*[paths for paths in self.paths.values()]))
                else:
                    self.path = random.choice(path_list)
            else:
                path_list = list(itertools.chain(*[paths for paths in self.paths.values()]))

            if len(path_list) != 0:
                self.path = random.choice(path_list)

        def object(self) -> ImageFont.truetype:
            if self.path:
                return ImageFont.truetype(self.path, size=self.size)
            else:
                print("!error : there are no font you selected.")
                return None

    # endregion

    Font: FontManager = None
    font_exist = False

    # region init
    def __init__(self,
                 fonts=None, font_list_tag: str = "None",
                 img_path: str = '', img: Image = None,
                 text: str = ''):
        """

        :param fonts:
        :param img_path:
        :param img:
        :param text:
        """
        # elements
        if not ImageManager.font_exist:
            ImageManager.Font = ImageManager.FontManager(fonts)
        else:
            pass
        self.Font: ImageManager.FontManager = ImageManager.Font

        self.img_original: Image
        self.img: Image

        self.texts: list = text.split('\n')
        self.text_bound_limit: tuple[float, float] = (0.8, 0.8)
        self.text_block_sizes: list[tuple[float, float]] = []

        # default setting
        self.settings = {
            'random font': True,
            'square img': True,
            'text in middle': True,
            'text vertical': False,
        }

        # setting elements
        if img_path:
            self.img_original = Image.open(img_path)
        elif img:
            self.img_original = img
        else:
            print("Warning : there's no img in here.")
            self.img_original = Image.open("")

        self.img = self.img_original

        # add_font
        if not fonts:
            pass
        elif type(fonts) is list:
            self.Font.add_fonts(fonts, tag=font_list_tag)
        elif type(fonts) is dict:
            self.Font.add_fonts_dict(fonts)

        if self.settings['random font']:
            self.Font.set_font_random()

    # endregion

    # region edit and add image

    def resize_image(self, size: tuple = (1024, 1024)):
        """
        resize image size (save in img)

        :param size: set size to (default is (1024,1024))
        :return: None
        """
        # add some features..
        img_size = self.img.size

        if self.settings['square img'] and img_size[0] == img_size[1]:
            self.img = self.img.resize(size)
            return

        if img_size[0] * size[1] > img_size[1] * size[0]:
            # if there is extra length size
            length = int(size[0] * (img_size[1] / size[1]))
            diff = int(img_size[0] - length) // 2
            self.img = self.img.crop((diff, 0, length + diff, img_size[1]))
        else:
            # if there is extra width size
            width = int(size[1] * (img_size[0] / size[0]))
            diff = int(img_size[1] - width) // 2
            self.img = self.img.crop((0, diff, img_size[0], width + diff))

        self.img = self.img.resize(size)
        return

    def open_image(self, img_path: str) -> None:
        """
        open image in image path (save in img, img_original)

        :param img_path: path of image file.
        :return: None
        """
        self.img_original = Image.open(img_path)
        self.img = self.img_original

    # endregion

    # region text in middle
    def add_text_in_middle(self, line=False, font_tags: list = None) -> None:
        draw = ImageDraw.Draw(self.img)
        font = self.Font.object()

        w_list, h_list = [], []
        for text in self.texts:
            text_w, text_h = draw.textsize(text, font=font)
            w_list.append(text_w)
            h_list.append(text_h)
        h_sum = sum(h_list)
        img_w, img_h = self.img.size

        self.update_text_blocks(draw)
        self.fit_text_font_size(draw)
        font = self.Font.object()

        h_sum = sum([size[1] for size in self.text_block_sizes])
        h_count = 0.0
        for text, size in zip(self.texts, self.text_block_sizes):
            draw.text(((img_w - size[0]) // 2, (img_h - h_sum) // 2 + h_count),
                      text, fill=(255, 255, 255), font=font)
            h_count += size[1]

    def update_text_blocks(self, draw: ImageDraw.Draw = None) -> None:
        if draw is None:
            return
        self.text_block_sizes = [draw.textsize(text, font=self.Font.object())
                                 for text in self.texts]

    def fit_text_font_size(self, draw: ImageDraw.Draw = None) -> None:
        img_w, img_h = self.img.size
        text_max_w = max([size[0] for size in self.text_block_sizes])
        text_max_h = max([size[1] for size in self.text_block_sizes])

        change_ratio = min([
            (img_w * self.text_bound_limit[0]) / text_max_w,
            (img_h * self.text_bound_limit[1]) / text_max_h,
            1.0
        ])
        self.Font.size = int(change_ratio * self.Font.size)

        if draw is not None:
            self.update_text_blocks(draw)

    # endregion
