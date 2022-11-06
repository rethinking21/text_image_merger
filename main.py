import os
from text_image_merge import ImageManager

FONT_PATH = './font/naver_handwriting'
TEMP_SELECT_FONT = './font'
IMG_TEST_PATH = './test/nightsky.jpg'

if __name__ == '__main__':
    fonts = {os.path.abspath(f'{FONT_PATH}/{font_path}'): "None"
             for font_path in os.listdir(FONT_PATH)
             if '.ttf' in font_path}
    ImageMan = ImageManager.ImageManager(img_path=IMG_TEST_PATH, fonts=fonts,
                                         text='줄바꿈을 해도\n자동으로 조절해서\n중앙으로 맞춰주는 프로그램.\n이렇게 이렇게 길이가 늘어나도 자동으로 조절해요 :)',)
    ImageMan.resize_image()
    ImageMan.add_text_in_middle(auto_font_color=True)
    ImageMan.img.show()
