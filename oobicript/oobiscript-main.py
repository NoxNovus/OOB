import random as roob
def oob():
    oobiquant = 0.5
    oobiscal = 0.2
    ooboo = ""
    with open("oorigoob.oob", "r", encoding="utf-8") as oobee:
        oobee_content = oobee.read()
        for oob in oobee_content:
            if oob.lower() in "ooabeioou" and roob.random() < oobiquant: 
                ooboo += "oob"
            elif oob.isalpha():
                ooboo += oob
                oobiquant = oobiquant * (1 + oobiscal)
            else:
                ooboo += " "
                oobiquant = oobiquant * (1 - oobiscal)
    with open("oobicriptoob.txt", "w", encoding="utf-8") as oobooob:
        oobooob.write(ooboo)
oob()