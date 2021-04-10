from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

my_username = '你的账号'
my_password = '你的密码'

driver = webdriver.Chrome()
driver.get("https://www.epubit.com/books")

# login
login_btn = driver.find_element(By.XPATH, '//i[text()="登录"]')
login_btn.click()

input_username = driver.find_element(By.XPATH, '//input[@id="username"]')
input_username.send_keys(my_username)

input_password = driver.find_element(By.XPATH, '//input[@id="password"]')
input_password.send_keys(my_password)

submit_btn = driver.find_element(By.XPATH, '//input[@id="passwordLoginBtn"]')
submit_btn.click()


# get course data
driver.get('https://www.epubit.com/course')
time.sleep(3)

item_list = driver.find_elements_by_css_selector('.course-list a')
course_data_list = []

while len(item_list) > 0:
    for item in item_list:
        link = item.get_attribute('href')
        img = item.find_element_by_tag_name('img').get_attribute('src')
        title = item.find_element_by_class_name('list-title').text
        price = item.find_element_by_class_name('price').text
        info = item.find_element_by_class_name('info').text
        course_data_list.append([link, img, title, price, info])
        print('==> {}'.format(title))

    next_page_btn = driver.find_element_by_css_selector('button.btn-next')

    if 'disabled' in next_page_btn.get_attribute('class'):
        print('last page')
        break
    else:
        next_page_btn.click()
        print('waiting...')
        time.sleep(3)
        item_list = driver.find_elements_by_css_selector('.course-list a')


print('total {} items'.format(len(course_data_list)))
driver.close()

with open('data.csv', mode='w') as data_file:
    writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    header = ['链接', '图片', '标题', '价格', '其他信息']
    writer.writerow(header)
    for item in course_data_list:
        writer.writerow(item)
