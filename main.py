import classes as cl

data = cl.load_from_json()

while True:
    chose = int(input("Здравствуйте, выберите действие: \n1-создать фильм\n2-создать сериал\n3-Вывести JSON\n4-Вывести XML\n"))
    if chose == 1:
        film = cl.Film()
        film.set_title()
        film.set_duration()
        film.set_rating()
        
        print("Вы ввели:", str(film))

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:    
                data["movies"].append(film.to_dict())
                cl.save_to_json(data)
                break
            elif xoj == 2:
                #Дописать xml
                print()
                break
            else:
                print("Неверный выбор")
        break
    elif chose == 2:
        print()
        break
    elif chose == 3:
        print()
        break
    elif chose == 4:
        print()
        break
    else:
        print("Неверный выбор")
    