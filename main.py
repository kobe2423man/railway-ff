import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def run_browser():
    print("正在准备启动 Firefox...")
    
    # 1. 设置 Firefox 选项 (极简模式，防内存溢出)
    options = Options()
    options.add_argument("--headless") # 无头模式，必须开
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 禁止加载图片和 CSS (最强省内存大法)
    options.set_preference("permissions.default.image", 2)
    options.set_preference("permissions.default.stylesheet", 2)

    # 2. 自动下载并启动驱动
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        # 获取你要跑的链接，如果没有设置变量，就默认跑谷歌
        url = os.getenv("IDX_URL", "https://www.google.com")
        print(f"正在打开: {url}")
        
        driver.get(url)
        
        # 等待 20 秒，假装在浏览
        time.sleep(20)
        
        print(f"成功访问，页面标题是: {driver.title}")
        
    except Exception as e:
        print(f"出错啦: {e}")
        
    finally:
        # 3. 必须彻底关闭，否则 Railway 内存会爆
        print("任务结束，关闭浏览器清理内存...")
        driver.quit()

if __name__ == "__main__":
    # 每隔 1 小时运行一次 (3600秒)
    # 这样既能保活，又不会因为一直开着浏览器导致内存溢出
    while True:
        run_browser()
        print("休息 1 小时...")
        time.sleep(3600)
