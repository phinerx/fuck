
import os
import time
try:
    import requests
    
except:
    print("\033[34mRequets installing...</>")
    os.system("pip install requets")
try:
    import httpx
except:
    print("Httpx instaling...</>")
try:
    from rich.progress import track
except:
    print("Rich installing...</>")
    os.system("pip install rich")
    from rich.progress import track
logo ="""
\033[1;31m     ██ ██ ██   ██ ██    ██ 
\033[33m     ██ ██ ██  ██  ██    ██ 
\033[1;33m     ██ ██ █████   ██    ██ 
\033[1;31m██   ██ ██ ██  ██  ██    ██ 
\033[35m █████  ██ ██   ██  ██████         
"""
def main():
    def working(pro="</>"):
        for i in track(range(500),description=pro):
            time.sleep(0.002)
        
    def tool():
        print("========================================================")
        print(logo)
        print("========================================================")
        print("[1]Casino_clone")
        print("[2]flask-app")
        print("[3]FB_DUMP")
        print("[4]text_enc")
        print("[5]fb_auto")
        a = input("CHOICE: ")
        if a in ["A","a","1"]:
            os.system("git clone https://github.com/phinerx/Casino_clone")
            os.system("cd Casino_clone")
            os.system("python main.py")
        if a in ["B","b","2"]:
            os.system("xdg-open https://github.com/phinerx/flask-app")
        if a in ["C","c","3"]:
            os.system("git clone https://github.com/phinerx/FB_DUMP")
            os.system("cd FB_DUMP")
            os.system("python main.py")
        if a in ["D","d","4"]:
            os.system("https://github.com/phinerx/text_enc")
            os.system("cd text_enc")
            os.system("python main.py")
        if a in ["E","e","5"]:
            os.system("git clone https://github.com/phinerx/fb_auto")
            os.system("cd fb_auto")
            os.system("python fb_auto_enc.py")
    def print_slowly(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1) 
    def admin():
        print("========================================================")
        print(logo)
        print("========================================================")
        time.sleep(1)
        text_line1 = "Hi I am Jakaria\n"
        text_line2 = "You can Call me Jiku\n"
        text_line3 = "I am a simple Coder\n"
        text_line4 = "My LifeLine is Suha\n"
        text_line5 = "You can call her S7HA\nHer old name was Sneha\nSo if you love me I will love you\n That is my rule"
        print_slowly(text_line1)
        print_slowly(text_line2)
        print_slowly(text_line3)
        print_slowly(text_line4)
        print_slowly(text_line5)
    def social():
        print("========================================================")
        print(logo)
        print("========================================================")
        print("[A]Facebook")
        print("[B]Instagram")
        print("[C]Telegram")
        social_input = input("CHOICE: ")
        if social_input in ["A","a","1"]:
            os.system("xdg-open https://www.facebook.com/mdjakaria.fiad")
        if social_input in ["B","b","2"]:
            os.system("xdg-open https://www.instagram.com/jiku__81/")
        if social_input in ["C","c","3"]:
            os.system("xdg-open https://t.me/@phiner7x")
            
        
    print("========================================================")
    print(logo)
    print("========================================================")
    print("[A]Tool")
    print("[B]Admin Info")
    print("[C]Social Media")
    print("[D]Wabsite")
    print("[X]Exit")
    user = input("CHOICE: ")
    if user in ["A", "a", "1"]:
        working()
        tool()
    if user in ["B","b","2"]:
        working()
        admin()
    if user in ["C","c","3"]:
        working()
        social()
    if user in ["D","d","4"]:
        working()
        os.system("xdg-open http://jikubro.great-site.net/?i=1")
    if user in ["X","x"]:
        exit()
    else:
        print("Choice Wrong!")
        main()
main()
