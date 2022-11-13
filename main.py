import os
from text_image_merge import ImageManager

FONT_PATH = './font/naver_handwriting'
WATERMARK_FONT = './watermark/consola.ttf'
TEMP_SELECT_FONT = './font'
IMG_TEST_PATH = './test/sky1.jpg'

if __name__ == '__main__':
    fonts = {os.path.abspath(f'{FONT_PATH}/{font_path}'): "None"
             for font_path in os.listdir(FONT_PATH)
             if '.ttf' in font_path}
    ImageMan = ImageManager.ImageManager(img_path=IMG_TEST_PATH, fonts=fonts)
    ImageMan.set_text('감성 글귀 넣기 좋은 글씨체로\n글귀를 이미지에 넣어보아요 :)')
    ImageMan.resize_image()
    ImageMan.add_color_img()
    ImageMan.add_text_in_middle(auto_font_color=True)
    ImageMan.add_watermark(font_path=os.path.abspath(WATERMARK_FONT))
    ImageMan.merge_img(2).save('./example_img/ex2.png')
