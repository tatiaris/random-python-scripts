from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)

def log_zybooks(user_name, pw):
    driver.get('https://learn.zybooks.com/signin')
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(user_name)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(pw)
    driver.find_element_by_xpath('//button[@class="signin-button zb-button primary raised full-width ember-view"]').click()
    time.sleep(3)

def show_answers():
    show_answer_buttons = driver.find_elements_by_xpath('//button[@class="show-answer-button zb-button secondary ember-view"]')
    for b in show_answer_buttons:
        b.send_keys('\n\n')

def get_answers():
    answer_list = driver.find_elements_by_xpath('//span[@class="forfeit-answer"]')
    for i in range(len(answer_list)):
        answer_list[i] = get_text_excluding_children(driver, answer_list[i])
    return answer_list

def input_answers(lst):
    input_elements = driver.find_elements_by_xpath('//textarea[@class="zb-text-area hide-scrollbar ember-text-area ember-view"]')
    for i in range(len(input_elements)):
        input_elements[i].send_keys(lst[i] + '\n')

def solve_free_response():
    show_answers()
    answers = get_answers()
    input_answers(answers)

def solve_multiple_choice():
    show_answer_buttons = driver.find_elements_by_xpath('//input[@type="radio"]')
    for b in show_answer_buttons:
        b.send_keys(' ')

def check_2x():
    time.sleep(1)
    checks = driver.find_elements_by_xpath('//div[@class="zb-checkbox grey label-present right ember-view"]')
    for c in checks:
        c.click()

def start_animations():
    s_buttons = driver.find_elements_by_xpath('//button[@class="start-button start-graphic zb-button primary raised ember-view"]')
    for b in s_buttons:
        b.send_keys('\n')

def continue_animations(n):
    i = 0
    while(len(driver.find_elements_by_xpath('//div[@class="play-button rotate-180 "]')) < n):
        try:
            driver.find_element_by_xpath('//div[@class="play-button  bounce"]').click()
        except Exception as e:
            i += 1

def get_num_animations():
    return len(driver.find_elements_by_xpath('//button[@class="start-button start-graphic zb-button primary raised ember-view"]'))

def solve_animations():
    check_2x()
    n = get_num_animations()
    start_animations()
    time.sleep(1)
    continue_animations(n)

# user_name = input('Enter username: ')
# pw = input('Enter password: ')
# course = input('Enter course: ')
# chapter = input('Enter chapter number: ')
# s_section = int(input('Start on section: '))
# e_section = int(input('End on section: '))
user_name = "nickzad.r@tamu.edu"
pw = "Zalaxy21y"
course = "TAMUCSCE111LightfootFall2019"
chapter = "4"
s_section = 1
e_section = 10
c_url = 'https://learn.zybooks.com/zybook/' + course + '/chapter/' + chapter + '/section/'

driver = webdriver.Chrome()
log_zybooks(user_name, pw)

for i in range(s_section, e_section + 1):
    try:
        driver.get(c_url + str(i))
        time.sleep(3)

        solve_animations()
        solve_free_response()
        solve_multiple_choice()

        print('Completed chapter', chapter, 'section', i)

        time.sleep(10)
    except Exception as e:
        print('Unable to complete chapter', chapter, 'section', i)
        print(e)

driver.quit()
