from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.PhantomJS()
import re


driver.get("http://www.17k.com/list/2943372.html")
# 获取总章数
getSumPage_text = driver.find_element_by_class_name("Volume").find_element_by_class_name("info").text
getSumPage_text = int(re.sub("\D", "", getSumPage_text))
print(getSumPage_text)
# # 获取章数
# getPage_text = driver.find_element_by_class_name("Volume").find_element_by_xpath("dd").text
# print(getPage_text)

# 测试获取文章内容
# driver.get("http://www.17k.com/chapter/2943372/37167082.html")
# test = driver.find_element_by_class_name("area").find_element_by_id("readArea").find_element_by_class_name(
#     "p").text
# print(test)
# 测试文章内容点击下一页
# jumpbtn = driver.find_element_by_class_name("NextPrevBtn").find_element_by_xpath("ul").find_element_by_xpath("li[@class='next']").find_element_by_xpath('a')  # 跳转到按钮
# jumpbtn.click()
# print(jumpbtn)
# print(driver.find_element_by_class_name("area").find_element_by_id("readArea").find_element_by_class_name(
#                 "p").text)



# 循环文章得到所有的页面
driver.get("http://www.17k.com/chapter/2943372/36919303.html")
def getData(start, end):
    for x in range(start,end+1):
        jumpbtn = driver.find_element_by_class_name("NextPrevBtn").find_element_by_xpath("ul").find_element_by_xpath(
            "li[@class='next']").find_element_by_xpath('a')  # 跳转到按钮
        jumpbtn.click()
        with open("./htmls/{0}.txt".format(x),'wb') as f:
            print(x)
            f.write(driver.find_element_by_class_name("area").find_element_by_id("readArea").find_element_by_class_name(
                "p").text.encode('utf-8'))
            f.close()

getData(1, getSumPage_text)