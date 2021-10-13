import random

moznosti = ["kámen", "nůžky", "papír"]
#print(volba_pocitace)

konec_cele_hry = False

while not konec_cele_hry:
    volba_hry = input("Zvol možnost(1-počítač proti počítači, 2-hráč proti počítači, 3-hráč proti hráči)/konec: ")

    if volba_hry == "konec":
        konec_cele_hry = True
    elif volba_hry == "2":
        konec_hry_2 = False
        while konec_hry_2 == False:
            volba_pocitace = random.choice(moznosti)
            volba_hrace = input("\nZvolte možnost(kámen, nůžky, papír)/konec: ")

            print("Hráč zvolil: {hrac}, počítač zvolil: {pocitac}".format(hrac=volba_hrace,
                                                                          pocitac=volba_pocitace))
            if volba_hrace == "konec":
                print("konec\n")
                konec_hry_2 = True
            
            elif volba_hrace == "kámen":
                if volba_pocitace == "kámen":
                    print("remíza")
                if volba_pocitace == "nůžky":
                    print("hráč vyhrává")
                if volba_pocitace == "papír":
                    print("počítač vyhrává")
                
            elif volba_hrace == "nůžky":
                if volba_pocitace == "kámen":
                    print("počítač vyhrává")
                if volba_pocitace == "nůžky":
                    print("remíza")
                if volba_pocitace == "papír":
                    print("hráč vyhrává")

                
            elif volba_hrace == "papír":
                if volba_pocitace == "kámen":
                    print("hráč vyhrává")
                if volba_pocitace == "nůžky":
                    print("počítač vyhrává")
                if volba_pocitace == "papír":
                    print("remíza")
                
            else:
                print("chybná volba")

    elif volba_hry == "1":
        pocitac1=random.choice(moznosti)
        pocitac2=random.choice(moznosti)
        print("Počítač 1 zvolil: {pocitac1}, počítač 2 zvolil: {pocitac2}".format(pocitac1=pocitac1,
                                                                          pocitac2=pocitac2))

        if pocitac1 == "kámen":
            if pocitac2 == "kámen":
                print("remíza")
            if pocitac2 == "nůžky":
                print("hráč vyhrává")
            if pocitac2 == "papír":
                print("počítač vyhrává")
                
        elif pocitac1 == "nůžky":
            if pocitac2 == "kámen":
                print("počítač vyhrává")
            if pocitac2 == "nůžky":
                print("remíza")
            if pocitac2 == "papír":
                print("hráč vyhrává")

                
        elif pocitac1 == "papír":
            if pocitac2 == "kámen":
                print("hráč vyhrává")
            if pocitac2 == "nůžky":
                print("počítač vyhrává")
            if pocitac2 == "papír":
                print("remíza")
        elif volba_hry == "konec":
            print("konec\n")
            konec_cele_hry = True
            break
        
    elif volba_hry == "3":
        konec_hry_3 = False
        while konec_hry_3 == False:
            hrac1 = input("\nHráč 1: Zvolte možnost(kámen, nůžky, papír)/konec: ")
            print("\n"*50)
            hrac2 = input("\nHráč 2: Zvolte možnost(kámen, nůžky, papír)/konec: ")

            print("Hráč 1 zvolil: {hrac1}, hráč 2 zvolil: {hrac2}".format(hrac1=hrac1,
                                                                          hrac2=hrac2))
            if hrac1 == "konec" or hrac2 == "konec":
                print("konec\n")
                konec_hry_3 = True
            
            elif hrac1 == "kámen":
                if hrac2 == "kámen":
                    print("remíza")
                if hrac2 == "nůžky":
                    print("hráč 1 vyhrává")
                if hrac2 == "papír":
                    print("hráč 2 vyhrává")
                
            elif hrac1 == "nůžky":
                if hrac2 == "kámen":
                    print("hráč 2 vyhrává")
                if hrac2 == "nůžky":
                    print("remíza")
                if hrac2 == "papír":
                    print("hráč 1 vyhrává")

                
            elif hrac1 == "papír":
                if hrac2 == "kámen":
                    print("hráč 1 vyhrává")
                if hrac2 == "nůžky":
                    print("hráč 2 vyhrává")
                if hrac2 == "papír":
                    print("remíza")
                
            else:
                print("chybná volba")

    
    else:
        print("chybná volba, napiš 1 nebo 2 nebo konec")
