# -*- coding: euc-kr -*-
import pyperclip, requests, json, os
from os.path import dirname
from PyQt5.QtCore import QThread, pyqtSignal

class Thread(QThread):
    threadEvent = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.is_id_initialied = False
        self.update_flag = False
        self.source = ""
        self.lang = "en"
        try:
            with open(f'{dirname(__file__)}/../config.json', "r") as cf:
                configs = json.load(cf)
                self.papago_id = configs['papago_id']
                self.papago_secret = configs['papago_secret']
                self.is_id_initialied = True
        except KeyError:
            raise Exception('papago_id or papago_secret is empty')
        except:
            raise Exception("Failed to read '../config.json'.")

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
            return f"[Translator] 에러입니다.\n{response.text}"

    def is_updated(self):
        return self.update_flag

    def get_lang(self):
        return self.lang

    def change_lang(self):
        if self.lang == "en":
            self.lang = "ja"
        else:
            self.lang = "en"
