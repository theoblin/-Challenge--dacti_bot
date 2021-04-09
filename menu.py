import os
from main import Program

os.system('cls')
print('$$$$$$$\                        $$\     $$\        $$$$$$$\             $$"\"')
print("$$  __$$\                       $$ |    \__|       $$  __$$\            $$ |")
print('$$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$\        $$ |  $$ | $$$$$$\ $$$$$$"\"')
print("$$ |  $$ | \____$$\ $$  _____|\_$$  _|  $$ |       $$$$$$$\ |$$  __$$\\_$$  _|")
print("$$ |  $$ | $$$$$$$ |$$ /        $$ |    $$ |       $$  __$$\ $$ /  $$ | $$ |")
print("$$ |  $$ | $$$$$$$ |$$ /        $$ |    $$ |       $$  __$$\ $$ /  $$ | $$ |")
print("$$$$$$$  |\$$$$$$$ |\$$$$$$$\   \$$$$  |$$ |       $$$$$$$  |\$$$$$$  | \$$$$  |")
print("\_______/  \_______| \_______|   \____/ \__|$$$$$$\\_______/  \______/   \____/")
print("                                           \______|")
print("")
print("              [1]       Simple test")
print("              [2]       Challenge online")
print("              [3]       Anticheat program")
print("")
print("")

choice = input("Choose a program: ")

#Simple test
if choice == "1":
    speed = input("Speed ? (0 : very fast > 1: very slow) : ")
    program = Program()
    program.connect(program.driver)
    program.driver.get('https://10fastfingers.com/typing-test/french')
    program.allow_cookies()
    program.create_words_list()
    program.insert_and_submit('//*[@id="inputfield"]', program.wordlist, speed)
#Competition
if choice == "2":
    os.system('cls')
    program = Program()
    program.connect(program.driver)
    program.allow_cookies()
    program.driver.get('https://10fastfingers.com/competitions')
    program.create_table(["n°", "Participants", "Tests done", "Time left"],'//*[@id="join-competition-table"]/tbody')
    n = input('Join competition n°: ')
    program.join_competition(n)
    program.create_words_list()
    speed = input("Speed ? (0 : very fast > 1: very slow) : ")
    program.insert_and_submit('//*[@id="inputfield"]', program.wordlist, speed, True)
#Anticheat
if choice == "3":
    print("[1] Simple")
    print("[2] Custom")
    print("[3] Competition")
    choice = input("Choose: ")
    # Simple test anticheat
    if choice == "1":
        speed = input("Speed ? (0 : very fast > 1: very slow) : ")
        program = Program()
        program.connect(program.driver)
        program.driver.get('https://10fastfingers.com/anticheat/view/1/3')
        program.allow_cookies()
        program.get_anticheat_img()
        program.read_img()
        program.insert_and_submit('//*[@id="word-input"]', program.wordlist,speed, True)
    if choice == "2":
        speed = input("Speed ? (0 : very fast > 1: very slow) : ")
        program = Program()
        program.connect(program.driver)
        program.driver.get('https://10fastfingers.com/anticheat/view/1/3')
        program.allow_cookies()
        program.get_anticheat_img()
        program.read_img()
        program.insert_and_submit('//*[@id="word-input"]', program.wordlist,speed, True)
    # Competition anticheat
    if choice == "3":
        speed = input("Speed ? (0 : very fast > 1: very slow) : ")
        program = Program()
        program.connect(program.driver)
        program.driver.get('https://10fastfingers.com/anticheat')
        #program.btn_click(program.driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/table/tbody').find_elements_by_tag_name('td')[0].find_elements_by_class_name('btn')[0])
        table = program.driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/table/tbody')
        table.find_elements_by_tag_name('td')[0].find_elements_by_class_name('btn')[0].click()
        program.allow_cookies()
        program.get_anticheat_img()
        program.read_img()
        program.insert_and_submit('//*[@id="word-input"]', program.wordlist, speed, True)
