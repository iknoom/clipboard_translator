# clipboard_translator
 파파고 api를 활용한 반투명 클립보드 번역 앱

## 사용 방법

https://developers.naver.com/docs/papago/papago-nmt-api-reference.md

위 링크의 Papago 번역 API를 사용합니다.

API 레퍼런스 설명과 같이 API를 사용하려면 클라이언트 아이디와 클라이언트 시크릿이 필요합니다.

네이버 계정으로 클라이언트 아이디와 클라이언트 시크릿을 발급 받아서 다음 변수에 추가합시다.

```python
self.papago_id = "클라이언트 아이디"
self.papago_secret = "클라이언트 시크릿"
```

![image](https://user-images.githubusercontent.com/48780754/96372033-e8509700-119f-11eb-96a1-efacde55a2bb.png)

실행 후 번역할 문장을 [Ctrl + C]로 복사하면 번역 앱에 번역됩니다.

## 기타

* 왼쪽 슬라이더 : 투명도

* 오른쪽 슬라이더 : 폰트 크기

* 우클릭 메뉴 : 앱 종료, 언어 변경(일본어)
