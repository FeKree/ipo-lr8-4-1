import json
count = 0
with open("Marigold.json", "r", encoding="utf-8") as file:
    Marigold_data = json.load(file)
while True:
    print("""Выберите действие:
          1: Вывести все записи
          2: Вывести запись по полю
          3: Добавить запись 
          4: Удалить запись по полю
          5: Выйти из программы
          """)
    n = int(input("Введите номер: "))
    if n == 1:
        for i in Marigold_data:
            print(f"""
            Код: {i['id']}, 
            Имя: {i['name']},                       
            Фабрика: {i['manufacturer']}, 
            Заправлена: {i['is_petrol']},    
            Объем Бака: {i['tank_volume']} 
            """)
        count += 1
    elif n == 2:
        pr = False
        ind = 0
        id_num = int(input("Введите ID машины, которая требуется "))
        for i in Marigold_data:
            if id_num == i['id']:
                print(f"""
                Код: {i['id']}, 
                Имя: {i['name']},                       
                Фабрика: {i['manufacturer']}, 
                Заправлена: {i['is_petrol']},    
                Объем Бака: {i['tank_volume']} 
                """)
                pr = True
                break
            ind += 1
        count +=1
    elif n == 3:
        id_search = int(input("Введите номер машины: "))
        pr1 = False
        for i in Marigold_data:
            if i['id'] == id_search:
                pr1 = True
                break
        if pr1:
            print("Машина с таким ID уже занята.")
        else:
            name = input("Введите имя машины: ")  
            manufacturer = input("Введите завод изготовитель: ")  
            is_petrol = input("Введите, заправлена ли машина Да/Нет (Да напишите корректно): ")  
            tank_volume = float(input("Введите объем бака машины: "))  

            new_car = {
                'id': id_search,
                'name': name,
                'manufacturer': manufacturer,
                'is_petrol': True if is_petrol.lower() == 'Да' else False, 
                'tank_volume': tank_volume
            }

            Marigold_data.append(new_car) 
            with open("strike.json", 'w', encoding='utf-8') as output_file: 
                json.dump(Marigold_data, output_file, ensure_ascii=False, indent=2)
            print("Машина успешно добавлена.")
        count += 1    
    elif n == 4:
        pr2 = False
        id_delete = int(input("Введите ID машины, которую требуется удалить "))
        for i in Marigold_data:
            if id_delete == i['id']:
                Marigold_data.remove(i)
                pr2 = True
                break
        if not pr2:
            print("Данное ID не найдено.")
        else:
            with open("Marigold.json", 'w', encoding='utf-8') as output_file:
                json.dump(Marigold_data, output_file, ensure_ascii=False, indent=2)
            print("Машина удалена.")
        count += 1    

    elif n == 5:
        print(f"Программа завершила свою работу. Кол-во операций равно {count}.")
        break
    else:
        print("Требовалось ввести число от 1 до 5, введите повторно!")
