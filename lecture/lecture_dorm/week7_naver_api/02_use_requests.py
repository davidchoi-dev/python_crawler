import requests
from urllib.request import urlparse

keyword = "강남역 탁구장"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                   "X-Naver-Client-Secret":"8sUQqFukKQ"})
print(result.json())