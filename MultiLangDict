sozluk={}
turkceler = ["elma", "armut"]
ingilizceler =["apple", "pear"]
fransizcalar=["pomme","poire"]
ispanyolcalar=["manzana","pera"]

print("Ingilizce -> 1 " ,"Fransizca ->2 ","Ispanyolca -> 3")

while(len(sozluk)!=10000):
    secim=input("ceviri dilini seciniz")
    if(secim==1):
        sozluk = dict (zip(turkceler,ingilizceler))
        while(len(sozluk)!=10000):
            girilen=raw_input("bir sozcuk giriniz: ")
            if sozluk.has_key(girilen):
                print sozluk[girilen]
                flag=raw_input("cikmak istiyormusunuz (E/H)")
                if(flag=="E",flag=="e"):
                    break
                else:
                    continue
            else:
                karsilik=raw_input("ingilizcesini giriniz: ")
                sozluk[girilen]=karsilik
            break
  if(secim==2):
        sozluk = dict (zip(turkceler,fransizcalar))
        while(len(sozluk)!=10000):
            girilen=raw_input("bir sozcuk giriniz: ")
            if sozluk.has_key(girilen):
                print sozluk[girilen]
                flag=raw_input("cikmak istiyormusunuz (E/H)")
                if(flag=="E",flag=="e"):
                    break
                else:
                    continue
            else:
                karsilik=raw_input("fransizcasini giriniz: ")
                sozluk[girilen]=karsilik
            break
    if(secim==3):
        sozluk = dict (zip(turkceler,ispanyolcalar))
        while(len(sozluk)!=10000):
            girilen=raw_input("bir sozcuk giriniz: ")
            if sozluk.has_key(girilen):
                print sozluk[girilen]
                flag=raw_input("cikmak istiyormusunuz (E/H)")
                if(flag=="E",flag=="e"):
                    break
                else:
                    continue
            else:
                karsilik=raw_input("İspanyolcasini giriniz: ")
                sozluk[girilen]=karsilik
            break
