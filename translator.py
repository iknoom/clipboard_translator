import pyperclip, requests
from PyQt5.QtCore import QThread, pyqtSignal

class Thread(QThread):
    threadEvent = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.update_flag = False
        self.source = ""
        self.lang = "en"
        self.papago_id = ""
        self.papago_secret = ""

    def run(self):
        while True:
            clipboard = " ".join(pyperclip.paste().split())
            clipboard = clipboard[:100]
            self.update_flag = (self.source != clipboard)
            self.source = clipboard
            self.threadEvent.emit(self.source)
            self.msleep(500)

    def get_translate(self):
        self.update_flag = False
        try:
            url = "https://openapi.naver.com/v1/papago/n2mt"
            headers = {
                "X-Naver-Client-Id": self.papago_id,
                "X-Naver-Client-Secret": self.papago_secret
            }
            params = {
                "source": self.lang,
                "target": "ko",
                "text": self.source
            }
            response = requests.post(url, headers=headers, data=params)
            res = response.json()
            return res['message']['result']['translatedText']
        except:
            return "[Translator] 에러입니다."

    def is_updated(self):
        return self.update_flag

    def get_lang(self):
        return self.lang

    def change_lang(self):
        if self.lang == "en":
            self.lang = "ja"
        else:
            self.lang = "en"