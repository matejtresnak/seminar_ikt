password_input = None
password_count = 0
puk_count = 0
password = "ahoj"
puk = "dobrej"

while password_count != 3 and puk_count != 3:
    password_input = input("Zadej heslo: ")
    if password_input == password:
        print("ok")
        break
    else:
        print("špatně")
        #print(password_count)
    password_count += 1

    if password_count == 3:
        while puk_count != 3 or puk_input != puk:
            puk_input = input("Zadej puk: ")
            puk_count += 1
            if puk_input == puk:
                password_count = 0
                break
            if puk_count == 3:
                break
            else:
                print("špatně")
                #print(puk_count)
        

