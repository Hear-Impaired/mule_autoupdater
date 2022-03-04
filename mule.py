import traceback
import platform
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

""" slack 메세지 전송용"""
import sys
sys.path.append("/root/github_repository/slack_messenger")
from slack import slack


class Mule:
    main_url = 'https://www.mule.co.kr/'
    args = ['--headless', '--no-sandbox', '--disable-dev-shm-usage', '--mute-audio', 'disable-gpu',
            'lang=ko_KR', 'User_Agent: Mozilla/5.0 \(Windows NT 10.0; Win64; x64\) AppleWebKit/537.36 \(KHTML, like Gecko\) Chrome/91.0.4472.77 Safari/537.36']
    msgr = slack()

    def __init__(self, _id, _pw):
        self.id = _id
        self.pw = _pw

    def __del__(self):
        try:
            self.driver.quit()
        except Exception as e:
            excpt_str = traceback.format_exc()
            print(excpt_str)
            print("__del__ -> except\n", excpt_str)


    def setArgs(self):
        options = Options()
        for arg in self.args:
            options.add_argument(arg)
        if platform.processor().__eq__(''):
            self.driver = webdriver.Chrome(
                options=options, executable_path="/usr/bin/chromedriver")
        elif platform.processor().__eq__('Intel64 Family 6 Model 94 Stepping 3, GenuineIntel'):
            self.driver = webdriver.Chrome(
                options=options, executable_path="D:\Dev\Anaconda3\Library\\bin\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1920, 1080)

    def run(self):
        try:
            self.driver.get("https://www.mule.co.kr/")
            sleep(1)

            # 로그인 창 열기
            self.driver.find_element_by_css_selector(
                '#header > div.header-center.cf > ul > li.l-login').click()
            sleep(1)

            # ID / PW 입력
            self.driver.find_element_by_css_selector(
                '#login-user-id').send_keys(self.id)
            sleep(1)
            self.driver.find_element_by_css_selector(
                '#login-user-pw').send_keys(self.pw)
            sleep(1)

            # 로그인 버튼 클릭
            self.driver.find_element_by_css_selector(
                '#modal-login > div > div > div > div > div.left-box > a.login-bt.login').click()
            sleep(10)

            # 마이 뮬 메뉴로 가 내가 쓴 글 찾아 들어가기
            self.driver.find_element_by_css_selector(
                '#header > div.header-center.cf > ul > li.l-mymule').click()
            sleep(1)
            self.driver.find_element_by_css_selector(
                '#mymule > div.browse-wrapper > ul > li:nth-child(2) > a').click()
            sleep(1)
            self.driver.find_element_by_css_selector(
                '#mymule > div.content-wrapper > div:nth-child(4) > div.scroll-table > table > tbody > tr:nth-child(2) > td:nth-child(2) > a').click()
            sleep(1)

            # 최신글로 올리기 클릭
            self.driver.find_element_by_css_selector(
                '#board > div.body-wrapper-board.cf > div.market-btn-wrapper > div.btn-list > a:nth-child(1)').click()
            sleep(1)
            self.driver.switch_to.alert.accept()
            sleep(1)
            self.driver.switch_to.alert.accept()
            sleep(1)

            # 로그아웃 하기
            self.driver.find_element_by_css_selector(
                '#header > div.header-center.cf > ul > li.l-logout').click()
            sleep(1)
            self.driver.switch_to.alert.accept()
            sleep(1)

            # slack에 완료 메세지 보내기
            self.msgr.post_message("#암호화폐", f"Mule : ID: {self.id} 끌어올리기 완료.")

        except Exception as e:
            excpt_str = traceback.format_exc()
            self.msgr.post_message("#암호화폐", f"Mule : except 발생!!!\n{excpt_str}")

        finally:
            try:
                self.driver.quit()
            except Exception as e:
                excpt_str = traceback.format_exc()
                self.msgr.post_message("#암호화폐", f"finally -> except!!!\n{excpt_str}")