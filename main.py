import os
from text_image_merge import ImageManager

FONT_PATH = './font/naver_handwriting'
IMG_TEST_PATH = './test/high1.jpg'

if __name__ == '__main__':
    fonts = [font_path for font_path in os.listdir(FONT_PATH)
             if '.ttf' in font_path]
    ImageMan = ImageManager.ImageManager(img_path=IMG_TEST_PATH, fonts=fonts)

    ImageMan.resize_image()
    ImageMan.main_img.show()