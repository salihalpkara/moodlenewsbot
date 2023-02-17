from selenium import webdriver
from bs4 import BeautifulSoup
import discord
import time
from datetime import datetime

client = discord.Client()


options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options= options)

username = "salih.kara"
password = "********"
mainpage = "http://moodle.tedronesans.k12.tr/moodle/my/"
degisiklik = ""

tde = {"dersadı":"Türk Dili ve Edebiyatı","moodlelink": "http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=192", "attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/tdeattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/tdecontent.txt"}
dkab =  {"dersadı":"Din Kültürü ve Ahlak Bilgisi","moodlelink": "http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=197","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/dkabattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/dkabcontent.txt"}
tarih = {"dersadı":"Tarih","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=200","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/tarihattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/tarihcontent.txt"}
felsefe ={"dersadı":"Felsefe","moodlelink": "http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=198","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/felsefeattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/felsefecontent.txt"}
pdr = {"dersadı":"Rehberlik","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=201","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/pdrattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/pdrcontent.txt"}
fizik = {"dersadı":"Fizik","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=226","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/fizikattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/fizikcontent.txt"}
ispanyolca = {"dersadı":"İspanyolca","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=194","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/ispanyolcaattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/ispanyolcacontent.txt"}
matematik = {"dersadı":"Matematik","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=190","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/matematikattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/matematikcontent.txt"}
ingilizce = {"dersadı":"İngilizce","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=189","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/ingilizceattachment.txt", "contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/ingilizcecontent.txt"}
kimya = {"dersadı":"Kimya","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=186","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/kimyaattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/kimyacontent.txt"}
müzik = {"dersadı":"Müzik","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=184","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/muzikattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/muzikcontent.txt"}
beden = {"dersadı":"Beden Eğitimi","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=183","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/bedenattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/bedencontent.txt"}
biyoloji = {"dersadı":"Biyoloji","moodlelink":"http://moodle.tedronesans.k12.tr/moodle/course/view.php?id=182","attachmentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/biyolojiattachment.txt","contentfile": "D:/Program Files/vs code file/Python/.vscode/.vscode/dersler/biyolojicontent.txt"}

def login():
    browser.get("http://moodle.tedronesans.k12.tr/moodle/login/index.php")
    time.sleep(2)
    usernamepart = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[1]/input")
    passwordpart = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[2]/input")
    loginbutton = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/button")
    usernamepart.send_keys(username)
    passwordpart.send_keys(password)
    loginbutton.click()

async def checklessons(ders):
    now = datetime.now()
    currenttime = now.strftime("%H:%M:%S")   
    global degisiklik
    browser.get(ders["moodlelink"])
    time.sleep(1)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    tumdersicerigi = soup.find(class_="course-content")
    temizdersicerigi = tumdersicerigi.text
    temizdersicerigibolunmus = temizdersicerigi.splitlines()
    oldcontent = []
    newcontent = []
    
    # #halihazırdaki site içeriği contentfile.txt dosyasında saklanıyor.
    # with open(ders["contentfile"],"w", encoding="utf-8") as f:
    #     for item in temizdersicerigibolunmus:
    #         f.write(item+ "\n" )
    #     f.close()
    
    #anlık site içeriği attachmentfile.txt dosyasına kaydedilecek.
    with open(ders["attachmentfile"],"w", encoding="utf-8") as f:
        for item in temizdersicerigibolunmus:
            f.write(item+ "\n" )
        f.close()
    
    #contentfile.txt dosyasının içeriğine oldcontent denecek.
    with open(ders["contentfile"],"r", encoding="utf-8") as f:
        oldcontent = f.read().splitlines(keepends=0)
    
    #attachmentfile.txt dosyasının içeriğine newcontent denecek.
    with open(ders["attachmentfile"],"r", encoding="utf-8") as f:
        newcontent = f.read().splitlines(keepends=0)

    difference = []
    for item in oldcontent:       
        if item in newcontent:
            difference = newcontent.remove(item)
    
    print(newcontent)
    print(len(newcontent))
    
    if len(newcontent) == 0:
        print(currenttime + " " + ders["dersadı"] + " dersinde değişiklik algılanamadı.")       
    else:
        print(currenttime + " " + ders["dersadı"] + " dersinde değişiklik algılandı. Algılanan değişiklik: ")            
        for item in newcontent:
            degisiklik += item + "\n"
        await client.get_channel(766980113794596865).send(currenttime + " saatinde" + "**" + ders["dersadı"] + "**" + " dersinde değişiklik algılandı.\n *Algılanan değişiklik:*\n\n " + degisiklik + "Ders Moodle sayfasına direkt erişim için: " + ders["moodlelink"])
        print(degisiklik)
        with open(ders["contentfile"], "w", encoding="utf-8") as f:
            for item in temizdersicerigibolunmus:
                f.write(item + "\n")
            f.close()
        degisiklik = ""
    
@client.event
async def on_ready():
    login()  
    while True:     
        await checklessons(tde)
        await checklessons(dkab)
        await checklessons(tarih)
        await checklessons(felsefe)
        await checklessons(fizik)
        await checklessons(ispanyolca)
        await checklessons(matematik)
        await checklessons(ingilizce)
        await checklessons(kimya)
        await checklessons(müzik)
        await checklessons(biyoloji)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options= options)
        browser.quit()
        time.sleep(1800)

client.run("***********************************************************")  