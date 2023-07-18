def verif(age):
    if age<1 :
        raise Exception("Tu serais pas un peu con ?")
    
    if age>99 :
        raise Exception("Toi tu te fous de ma gueule...")
    
    if age >18:
        print("Tu as sans doute le permis a ton age")
    
    elif age>0:
        print("BRavo champion tu sais faire du velo")