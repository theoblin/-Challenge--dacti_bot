#  $$$$$$$\                        $$\     $$\        $$$$$$$\             $$\
#  $$  __$$\                       $$ |    \__|       $$  __$$\            $$ |
#  $$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$\        $$ |  $$ | $$$$$$\ $$$$$$\
#  $$ |  $$ | \____$$\ $$  _____|\_$$  _|  $$ |       $$$$$$$\ |$$  __$$\\_$$  _|
#  $$ |  $$ | $$$$$$$ |$$ /        $$ |    $$ |       $$  __$$\ $$ /  $$ | $$ |
#  $$ |  $$ |$$  __$$ |$$ |        $$ |$$\ $$ |       $$ |  $$ |$$ |  $$ | $$ |$$\
#  $$$$$$$  |\$$$$$$$ |\$$$$$$$\   \$$$$  |$$ |       $$$$$$$  |\$$$$$$  | \$$$$  |
#  \_______/  \_______| \_______|   \____/ \__|$$$$$$\\_______/  \______/   \____/
#                                              \______|
#
#

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
import pytesseract
from PIL import Image
from io import BytesIO
from prettytable import PrettyTable

class Program:

    def __init__(self, wordlist=[]):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.wordlist = wordlist

    # Config
    pytesseract.pytesseract.tesseract_cmd = r'E:\programs\tesseract.exe'

    # Connect to website account
    def connect(self, driverName):
        driverName.get('https://10fastfingers.com/login')
        driverName.find_element_by_xpath('//*[@id="UserEmail"]').send_keys('')
        driverName.find_element_by_xpath('//*[@id="UserPassword"]').send_keys('')
        self.btn_click('//*[@id="login-form-submit"]')

    #Remove cookies popup
    def allow_cookies(self):
        time.sleep(1)
        self.btn_click('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')

    def btn_click(self, btnXpath):
        btn = self.driver.find_element_by_xpath(btnXpath)
        btn.click()

    # Anticheat module
    def get_anticheat_img(self):
        time.sleep(1)
        btnstart = self.driver.find_element_by_xpath('//*[@id="start-btn"]')
        btnstart.click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="word-img"]/img')
        element = self.driver.find_element_by_xpath('//*[@id="word-img"]/img')
        location = element.location
        size = element.size
        png = self.driver.get_screenshot_as_png()  # saves screenshot of entire page
        im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))  # defines crop points
        im.save('anticheat_imgs/1.png')  # saves new cropped image

    # Read image
    def read_img(self):
        img = cv2.imread('anticheat_imgs/1.png')
        text = pytesseract.image_to_string(img)
        time.sleep(2)
        arrayv1 = text.split(" ")
        arrayv2 = []
        for word in arrayv1:
            if ("\n") in word:
                split = word.split('\n')
                for word in split:
                    arrayv2.append(word)
            else:
                arrayv2.append(word)
        arrayv2.remove('\x0c')
        self.wordlist = arrayv2


    # Create word list
    def create_words_list(self):
        time.sleep(1)
        parent = self.driver.find_element_by_xpath('//*[@id="words"]')
        elementList = parent.find_elements_by_tag_name("span")
        for word in elementList:
            self.wordlist.append(word.get_attribute('innerHTML'))

    # Enter word in input
    def insert_and_submit(self, inputXpath, wordList, speed=1, final=False):
        time.sleep(0.5)
        inputElement = self.driver.find_element_by_xpath(inputXpath)
        for word in wordList:
            time.sleep(float(speed))
            inputElement.send_keys(word)
            inputElement.send_keys(Keys.SPACE)
        if final != False:
            inputElement.send_keys(Keys.TAB, Keys.ENTER)

    #Create a graphic table of all availables competitions
    def create_table(self, headers,xpath):
        i = 1
        local_table = PrettyTable()
        local_table.field_names = headers
        table = self.driver.find_element_by_xpath(xpath)
        online_table = table.find_elements_by_tag_name('tr')
        for row in online_table:
            row2 = row.find_elements_by_tag_name('td')
            local_table.add_row([i, row2[3].text, row2[4].text, row2[5].text])
            i+=1
        print(local_table)

    #Join a competition
    def join_competition(self, num_or_link):
       if len(num_or_link) > 3 : #If link is sent
        self.driver.get('https://10fastfingers.com/competition/' + num_or_link + '/')
       else: #if number is sent
        self.driver.get('https://10fastfingers.com/competitions')
        self.driver.find_element_by_xpath(
           '//*[@id="join-competition-table"]/tbody/tr[' + num_or_link + ']/td[2]/a').click()







