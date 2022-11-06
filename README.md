# text image merger 🖼️

 ---
## 사용 방법

main.py에 예제 코드를 넣었습니다!
<br>ImageManager를 옮겨서 사용할 수 있습니다

## 주요 코드

#### ImageManager() 생성자
<b>그림 설정</b>
<br>img_path="이미지의 코드" 또는 Image="pil 이미지 값 (PIL.Image)" 을 이용하여 이미지를 불러올 수 있습니다.
<br><br><b>폰트설정</b>
<br> fonts=리스트, font_list_tag=태그 이름(기본은 'None') 또는
<br> fonts=딕셔너리({'폰트절대주소' : '태그값'}) 으로 폰트를 불러올 수 있습니다.

<b>텍스트 설정</b>
<br> text='텍스트' 를 통하여 텍스트를 넣을 수 있습니다.
자동 줄바꿈이 되지 않아 줄바꿈시 '\n' 을 넣어주어야 합니다.


#### ImageManager.resize_image(size=(1024,1024))
그림을 size의 크기로 잘라줍니다.


#### ImageManager.add_text_in_middle(auto_font_color=False)
그림에 넣어진 텍스트를 중앙에 배치되도록 설정합니다.
<br> add_text_in_middle 를 통해 글씨 색상을 자동으로 정해주게 합니다. (False시, 기본값 흰색으로 설정)

#### ImageManager.img.show()
이미지를 보여줍니다 (ImageManager.img는 PIL.Image 임)