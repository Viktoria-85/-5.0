from time import sleep

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://ya.ru')
sleep(5)

driver.fullscreen_window()

sleep(5)

driver.save_screenshot('./ya.png')



# driver.minimize_window()

# for x in range(1, 10):
#  driver.back()
#  driver.forward()
#  driver.refresh()

# driver.set_window_size(640, 460)






