from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import psycopg2
import time
import os

teacher = []

def collect():

    # DB
    db = psycopg2.connect(host=os.getenv("DB_HOST"), dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), port=os.getenv("DB_PORT"))
    db.autocommit=True
    cur = db.cursor()

    # 크롬 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument("disable_gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get('https://dsmhs.djsch.kr/login.do?s=dsmhs')

    action = ActionChains(driver)

    # 로그인
    # driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/header/div[2]/ul/li[2]/a').click()
    driver.find_element_by_name('imemUsrID').send_keys(os.getenv("ID"))
    driver.find_element_by_name('imemUsrPass').send_keys(os.getenv("PW"))
    driver.find_element_by_class_name('btn_submit').click()

    # alert 넘기기
    for i in range(0, 3):
        if EC.alert_is_present():
            result = driver.switch_to.alert
            result.accept()
    
    time.sleep(1)
    
    driver.get('https://dsmhs.djsch.kr/sub/info.do?m=0905&s=dsmhs') # 과제제출로 이동

    div = driver.find_element_by_xpath('//*[@id="subContent"]/div[2]/div[2]/div/div')

    for table in div.find_elements_by_tag_name("table"):
        tbody = table.find_element_by_tag_name("tbody")
        for tr in tbody.find_elements_by_tag_name("tr"):
            name = tr.text.split()[0]
            teacher.append(name)

    print(teacher)
    
    query = """
    INSERT INTO teacher(name, year) VALUES(%s, %s);
    """
    year = str(date.today().year)
    for i in range(len(teacher)):
        cur.execute(query, [teacher[i], year])

if __name__ == "__main__":
    collect()
