from playsound import playsound as play
import datetime
import time

timerhour = int(input("Lütfen Saati Giriniz"))
timerminute = int(input("Lütfen Dakikayı Giriniz"))

while True:

    
    timenow = datetime.datetime.now()

    hournow = timenow.hour
    minutenow = timenow.minute

    #def bitir(): #Bitirme fonksiyonu (daha çalışmıyor)
    #    g_bitir = input("Bitirmek İçin G ye Basın:")
        
    #    if  g_bitir == "G":

    #        quit()



    if hournow == timerhour and minutenow == timerminute:
        print("Kalkma Vakti")
        print("Şuanda Saat : ", hournow , ":", minutenow)
        
        play("C:\\Users\\technopc\\Desktop\\YAZILIM\\Python\\Projeler\\Alarm\\songul3.mp3")


        
    
    
        

    

    
        





