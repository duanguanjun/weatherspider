# *_* coding:utf-8 *_*

# 开发团队:中国软件开发团队
# 开发人员:Administrator
# 开发时间:2019/3/25 7:18
# 文件名称:weathercityqury
# 开发工具:PyCharm
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import re


def main():
    # 初始化浏览器对象
    # desired_cap = DesiredCapabilities.PHANTOMJS.copy()
    # driver = webdriver.PhantomJS(desired_capabilities=desired_cap)
    # 修改请求头中的UA
    # desired_cap[
    #     'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 设置其他请求投信息,其中key为要修改的请求投键名
    # desired_cap['phantomjs.page.customHeaders.{}'.format(key)] = 'xxxx'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #
    # 更换头部
    chrome_options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"')

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)
    driver.get("http://www.weather.com.cn")
    # 生成屏幕快照文件
    # driver.get_screenshot_as_file('01.png')
    # 通过class name 方式定位
    element = driver.find_element_by_class_name("city_name")  # .send_keys("selenium")
    print(type(element))
    print(element)
    # element.send_keys("selenium")

    text = driver.page_source
    # print(text)
    '''
    <span class="city_name"><em>深圳</em></span>
    '''
    result = re.findall('<span class="city_name"><em>(.*?)</em></span>', text, re.S)
    print(result[0])
    driver.close()

    # driver = webdriver.PhantomJS(desired_capabilities=desired_cap)

    # html=driver.get('http://www.weather.com.cn')


if __name__ == '__main__':
    main()
