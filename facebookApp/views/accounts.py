from django.shortcuts import render, redirect, get_object_or_404
from facebookApp.models import Accounts
from pathlib import Path

from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import random
import json
import time

codelist = ['US-C', 'US', 'US-W']

#muestra usuarios
def accounts(request):
    accounts = Accounts.objects.all()
    script = ""
    for x in accounts:
        script += x.email + "/" + x.password + "; "
    
    script = script[:-2]

    return render(
        request,
        "accounts/accounts.html",
        {"accounts": accounts, "script": script},
    )

#guardar usuarios
def save_accounts(request):
    try:
        array = request.POST['accounts']
        accounts = array.split(';')
        for x in accounts:
            account = x.split('/')

            cuenta = Accounts()
            cuenta.email = account[0]
            cuenta.password = account[1]
            #-----------------------------------------------#
            codechoice = random.choice(codelist)
            #subprocess.call("windscribe connect " + codechoice, shell=True)

            geckodriver_autoinstaller.install()
            driver = webdriver.Firefox()
            time.sleep(18)
            driver.get('https://m.facebook.com/?wtsid=rdr_0AEeUDpTCPEHlzv6Y')

            email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
            email_input.send_keys(cuenta.email)

            password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
            password_input.send_keys(cuenta.password)

            login_btn = driver.find_element(By.NAME, 'login')
            login_btn.click()

            xs = driver.get_cookie("xs")
            c_user = driver.get_cookie("c_user")

            Path(f'xs.{cuenta.email}').write_text(json.dumps(xs))
            Path(f'c_user.{cuenta.email}').write_text(json.dumps(c_user))
            driver.quit()
            #-----------------------------------------------#
            cuenta.save()
            #subprocess.call("windscribe disconnect", shell=True)

        return redirect("accounts")
    except ValueError:
        return render(
            request, "accounts/accounts.html", {"accounts": accounts, "error": "Error al Guardar la informacion"}
        )

#detalle de cuentas
def detail_accounts(request, accounts_id):
    account = get_object_or_404(Accounts, pk=accounts_id)
    accounts = Accounts.objects.all()
    return render(
        request, "accounts/detail.html", {"account": account, "accounts": accounts}
    )

#Actualiza la informacion de usuario
def update_accounts(request, accounts_id):
    try:
        accounts = get_object_or_404(Accounts, pk=accounts_id)
        accounts.email = request.POST['email']
        accounts.password = request.POST['password']
        accounts.save()
        return redirect("accounts")
    except ValueError:
        return render(
            request, "accounts/detail.html", {"accounts": accounts, "error": "Error al actualizar la informacion"}
        )

#Elimina la informacion seleccionada
def delete_accounts(request, accounts_id):
    accounts = get_object_or_404(Accounts, pk=accounts_id)
    accounts.delete()
    return redirect("accounts")


