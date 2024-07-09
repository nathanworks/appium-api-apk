from appium import webdriver
# from appium.options.common.base import AppiumOptions 
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
import os

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

current_dir = os.path.dirname(__file__)

apk_path = os.path.join(current_dir, 'ApiDemos-debug.apk')

options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UiAutomator2",
	"appium:platformName": "Android",
	"appium:platformVersion": "10",
	"appium:deviceName": "8L8XQC5D9TMFY969",
	"appium:app": apk_path,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

menu_accessibility = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Access'ibility")
menu_accessibility.click()

back_button = ActionChains(driver)
back_button.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
back_button.w3c_actions.pointer_action.move_to_location(510, 1554)
back_button.w3c_actions.pointer_action.pointer_down()
back_button.w3c_actions.pointer_action.pause(0.1)
back_button.w3c_actions.pointer_action.release()
back_button.perform()

menu_text = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Text")
menu_text.click()
menu_text_longtextbox = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="LogTextBox")
menu_text_longtextbox.click()

field_longtextbox = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/text")
field_longtextbox.click()
field_longtextbox.send_keys("jonathan hermawan")

add_longtextbox = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
add_longtextbox.click()

driver.quit()