import collections

pets = {1: {'Мухтар': {"Вид питомца": 'Собака', "Возраст питомца": 1, "Имя владельца": "Михаил"}}, 2: {"Барсик": {"Вид питомца": "Кот", "Возраст питомца": 4, "Имя владельца": "Ольга"}}, 3: {"Каа": {"Вид питомца": "Синезубый Питон", "Возраст питомца": 7, "Имя владельца": "Маугли"}}}

# шпаргалка оставлю тут для себя..
#ID = int(input())
#print(list(pets.items())[ID - 1])
#print(pets[ID].items())

command = input("Введите комманду(create, list, read, delete, update, stop):")

#_______________________________________________________________________________________________________________
while command != "stop":
    if command == "create" or command == "list" or command == "delete" or command == "update" or command == "read":
        if command == "create":
            def create():
                PetsName = input('Имя питомца:')
                PetsType = input('Вид:')
                PetsAge = int(input('Возраст:'))
                OwName = input('Владелец:')

                last = collections.deque(pets, maxlen=1)[0]
                last += 1
                pets[last] = {PetsName: {"Вид питомца": PetsType, "Возраст питомца": PetsAge, "Имя владельца": OwName}}
                print(pets)
            
            create()
            command = input("Введите комманду(create, list, read, delete, update, stop):")
    #_______________________________________________________________________________________________________________
        elif command == "list":
            def pets_list():
                for s in pets.keys():
                    print(s, "-", pets[s])

            pets_list()
            command = input("Введите комманду(create, list, read, delete, update, stop):")
    #_______________________________________________________________________________________________________________
        else:

            Key = int(input("Введите номер записи питомца:"))   

            def get_pet():
                if Key in pets.keys():
                    return pets[Key]               
                else:        
                    print("Wrong key!")
                    return(0)
                             
    #_______________________________________________________________________________________________________________
            if command == "read" and get_pet() != 0:
                get_pet()
                def read():      
                
                    age = int(dict(list(pets[Key].values())[0])["Возраст питомца"])

                    def get_suffix():

                        if int(age) % 10 == 1:
                            return("год")
                        elif age % 10 > 1 and age % 10 < 5: 
                            return("года")
                        else:
                            return("лет")

                    print('Это', dict(list(pets[Key].values())[0])["Вид питомца"], 'по кличке',"'"+str(*list(pets[Key]))+"',", 'возраст питомца:', dict(list(pets[Key].values())[0])["Возраст питомца"], str(get_suffix())+".", 'Имя владельца:',  dict(list(pets[Key].values())[0])["Имя владельца"])
                read()
                command = input("Введите комманду(create, list, read, delete, update, stop):")

    #_______________________________________________________________________________________________________________
            elif command == "update" and get_pet() != 0:
                get_pet()
                def update():
     

                    PetsName = input('Новое имя питомца:')
                    PetsType = input('Новый вид:')
                    PetsAge = int(input('Новый возраст:'))
                    OwName = input('Новый владелец:')

                    pets[Key] = {PetsName: {"Вид питомца": PetsType, "Возраст питомца": PetsAge, "Имя владельца": OwName}}
    
                    print(pets)
                update()
                command = input("Введите комманду(create, list, read, delete, update, stop):")

    #_______________________________________________________________________________________________________________    
            elif command == "delete" and get_pet() != 0:
                get_pet()
                def delete():
                    del pets[Key]
                    print("Номер", Key, "удален!", "Обновленный словарь -", pets)
                delete()
                command = input("Введите комманду(create, list, read, delete, update, stop):")
    else:
        print("Wrong command!")
        command = input("Введите комманду(create, list, read, delete, update, stop):")
#_______________________________________________________________________________________________________________
else:
    print("Bye!")
