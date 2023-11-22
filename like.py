from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller
import orjson
from pathlib import Path

post = 'https://www.facebook.com/permalink.php?story_fbid=122101611290123078&id=61553692342844&ref=embed_post'

geckodriver_autoinstaller.install()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

# add_cookie method driver 
c_user = orjson.loads(Path('c_userangel1521ramos@gmail.com').read_bytes())
xs = orjson.loads(Path('xsangel1521ramos@gmail.com').read_bytes())

driver.add_cookie(c_user)
driver.add_cookie(xs)

driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

driver.get(post)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1r8uery x1iyjqo2 xs83m0k xeuugli xl56j7k x6s0dn4 xozqiw3 x1q0g3np xn6708d x1ye3gou xexx8yu xcud41i x139jcc6 x4cne27 xifccgj xn3w4p2 xuxw1ft']"))).click()

print('Post liked!')