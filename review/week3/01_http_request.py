# 실습1 http://www.naver.com에 request를 보내서 string을 받아오세요
# console에 출력 해보세요
from urllib.request import urlopen

url_design = "https://www.naver.com/nvthemecast_body?theme=DESIGN"
html = urlopen(url_design)
# 크롤링
print(html.read())

# parsing