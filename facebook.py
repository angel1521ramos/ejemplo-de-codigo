from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller

from pathlib import Path
import json


email = 'angel1521ramos@gmail.com'
password = 'Dsti2k22#'
post = 'https://www.facebook.com/permalink.php?story_fbid=122101611290123078&id=61553692342844&ref=embed_post'
#https://www.facebook.com/permalink.php?story_fbid=pfbid0CVshpnnu5ZUAP9zmX2H9AuLxZBL4GWNwaJNjyH15EsiqLGPSwaqMVAj23nY4gFsTl&id=61553692342844

geckodriver_autoinstaller.install()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys(email)

password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys(password)

login_btn = driver.find_element(By.NAME, 'login')
login_btn.click()

#wait.until(EC.url_changes('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y'))
#driver.get(post)
#
#wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1r8uery x1iyjqo2 xs83m0k xeuugli #xl56j7k x6s0dn4 xozqiw3 x1q0g3np xn6708d x1ye3gou xexx8yu xcud41i x139jcc6 x4cne27 xifccgj xn3w4p2 xuxw1ft']"))).click()
#
#print('Post liked!')

xs = driver.get_cookie("xs")
c_user = driver.get_cookie("c_user")

Path(f'xs{email}').write_text(json.dumps(xs)) 
Path(f'c_user{email}').write_text(json.dumps(c_user)) 

#driver.quit()
#angel1521ramos@gmail.com
#Dsti2k22#


