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

codelist = [ 'US']


def shares(request):
    try:
        urls = request.POST['url']
        accounts = Accounts.objects.all()

        for i in range(0, len(accounts), 3):
            for j in range(i, min(i + 3, len(accounts))):
                codechoice = random.choice(codelist)
                #subprocess.call("windscribe connect " + codechoice, shell=True)

                email = accounts[j].email
                password = accounts[j].password

                geckodriver_autoinstaller.install()
                driver = webdriver.Firefox()
                wait = WebDriverWait(driver, 30)
                driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

                email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
                email_input.send_keys(email)

                password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
                password_input.send_keys(password)

                login_btn = driver.find_element(By.NAME, 'login')
                login_btn.click()

                wait.until(EC.url_changes(
                    'https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y'))
                driver.get(urls)

                share = driver.find_element(By.XPATH, '//*[@id="mount_0_0_mk"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div/div/div[3]')
                share.click()

                share_btn = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Dv"]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]')
                share_btn.click()

                print(f"share de ... { email }")
                driver.quit()
                #subprocess.call("windscribe disconnect", shell=True)

            if i + 3 < len(accounts):
                print("espera 18 segundos ... se esta cambiando la direccion ip")
                time.sleep(18)

        webbrowser.open(urls)
        return redirect("accounts")
    except ValueError:
        return render(
            request, "actions/shares.html", {
                "error": "Error realizar la accion"}
        )

#dar share tweet
def share(request, accounts_id):
    try:
        codechoice = random.choice(codelist)
        #subprocess.call("windscribe connect " + codechoice, shell=True)
        urls = request.POST['url']
        account_select = Accounts.objects.get(id=accounts_id)

        email = account_select.email
        password = account_select.password

        geckodriver_autoinstaller.install()
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 30)
        driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

        email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
        email_input.send_keys(email)

        password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
        password_input.send_keys(password)

        login_btn = driver.find_element(By.NAME, 'login')
        login_btn.click()

        wait.until(EC.url_changes('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y'))
        driver.get(urls)

        share = driver.find_element(By.XPATH, '//*[@id="mount_0_0_mk"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div/div/div[3]')
        share.click()

        share_btn = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Dv"]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]')
        share_btn.click()

        print(f"share de ... { email }")
        driver.quit()

        #subprocess.call("windscribe disconnect", shell=True)
        webbrowser.open(urls)

        account = get_object_or_404(Accounts, pk=accounts_id)
        accounts = Accounts.objects.all()
        return render(
            request, "accounts/detail.html", {"account": account, "accounts": accounts}
        )
    except ValueError:
        return render(
            request, "actions/shares.html", {"error": "Error realizar la accion"}
        )
