# clipboard_translator
 파파고 api를 활용한 반투명 클립보드 번역 앱

## 사용 방법

https://developers.naver.com/docs/papago/papago-nmt-api-reference.md

위 링크의 Papago 번역 API를 사용합니다.

API 레퍼런스 설명과 같이 API를 사용하려면 클라이언트 아이디와 클라이언트 시크릿이 필요합니다.

네이버 계정으로 클라이언트 아이디와 클라이언트 시크릿을 발급 받아서 `config.json` 파일에 API 아이디와 비밀키를 추가합니다.

```json
// config.json
{
  "papago_id": "클라이언트 아이디",
  "papago_secret": "클라이언트 시크릿"
}
```

실행에 필요한 의존성 라이브러리들을 설치합니다.
```
pip3 install PyQt5 pyperclip
```

source/papago_translator.py 를 실행합니다.
```
python3 source/papago_translator.py
```

## 실행 예시

![image](https://user-images.githubusercontent.com/48780754/96372033-e8509700-119f-11eb-96a1-efacde55a2bb.png)

실행 후 번역할 문장을 [Ctrl + C]로 복사하면 번역 앱에 번역됩니다.

## 기타

* 왼쪽 슬라이더 : 투명도

* 오른쪽 슬라이더 : 폰트 크기

* 우클릭 메뉴 : 앱 종료, 언어 변경(일본어)

## 제한 사항

* 파파고 번역 API는 __일일 최대 10000글자__ 까지 번역하도록 제한되어 있습니다. (2020.10.19 파파고 API 정책 기준)
