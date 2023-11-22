from django.shortcuts import render, redirect, get_object_or_404
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from facebookApp.models import Accounts

import geckodriver_autoinstaller
import subprocess
import random
import webbrowser
import time
import orjson
from pathlib import Path

codelist = ['US-C', 'US', 'US-W']


def likes(request):
    try:
        urls = request.POST['url']
        accounts = Accounts.objects.all()

        for i in range(0, len(accounts), 3):
            for j in range(i, min(i + 3, len(accounts))):
                codechoice = random.choice(codelist)
                #subprocess.call("windscribe connect " + codechoice, shell=True)

                email = accounts[j].email
                #-----------------------------------------------#
                geckodriver_autoinstaller.install()
                driver = webdriver.Firefox()
                wait = WebDriverWait(driver, 10)
                driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

                # add_cookie method driver 
                c_user = orjson.loads(Path(f'c_user.{email}').read_bytes())
                xs = orjson.loads(Path(f'xs.{email}').read_bytes())

                driver.add_cookie(c_user)
                driver.add_cookie(xs)

                driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')
                driver.get(urls)

                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1r8uery x1iyjqo2 xs83m0k xeuugli xl56j7k x6s0dn4 xozqiw3 x1q0g3np xn6708d x1ye3gou xexx8yu xcud41i x139jcc6 x4cne27 xifccgj xn3w4p2 xuxw1ft']"))).click()

                print(f"like de ... { email }")
                driver.quit()
                #-----------------------------------------------#
                #subprocess.call("windscribe disconnect", shell=True)

            if i + 3 < len(accounts):
                print("espera 18 segundos ... se esta cambiando la direccion ip")
                time.sleep(18)

        return redirect("accounts")
    except ValueError:
        return render(
            request, "actions/likes.html", {
                "error": "Error realizar la accion"}
        )

#dar like tweet
def     like(request, accounts_id):
    try:
        codechoice = random.choice(codelist)
        #subprocess.call("windscribe connect " + codechoice, shell=True)
        urls = request.POST['url']
        account_select = Accounts.objects.get(id=accounts_id)

        email = account_select.email
        password = account_select.password

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

        wait.until(EC.url_changes('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y'))
        driver.get(urls)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1r8uery x1iyjqo2 xs83m0k xeuugli xl56j7k x6s0dn4 xozqiw3 x1q0g3np xn6708d x1ye3gou xexx8yu xcud41i x139jcc6 x4cne27 xifccgj xn3w4p2 xuxw1ft']"))).click()

        print(f"like de ... { email }")
        driver.quit()

        #subprocess.call("windscribe disconnect", shell=True)

        account = get_object_or_404(Accounts, pk=accounts_id)
        accounts = Accounts.objects.all()
        return render(
            request, "accounts/detail.html", {"account": account, "accounts": accounts}
        )
    except ValueError:
        return render(
            request, "actions/likes.html", {"error": "Error realizar la accion"}
        )
