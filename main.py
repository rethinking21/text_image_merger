import os
from text_image_merge import ImageManager

FONT_PATH = './font/naver_handwriting'
IMG_TEST_PATH = './test/high1.jpg'

if __name__ == '__main__':
    fonts = [os.path.abspath(f'{FONT_PATH}/{font_path}')
             for font_path in os.listdir(FONT_PATH)
             if '.ttf' in font_path]
    ImageMan = ImageManager.ImageManager(img_path=IMG_TEST_PATH, fonts=fonts, text='테스틍')

    ImageMan.resize_image()
    ImageMan.set_font_random()
    ImageMan.add_text_in_middle()
    ImageMan.return_img.show()
