import json
count = 0
end = True
with open("Marigold.json", "r", encoding="utf-8") as file:
    Marigold_data = json.load(file)
    def fir():
        global count 
        for i in Marigold_data:
            print(f"""
            Код: {i['id']}, 
            Имя: {i['name']},                       
            Фабрика: {i['manufacturer']}, 
            Заправлена: {i['is_petrol']},    
            Объем Бака: {i['tank_volume']}
            """)
        count += 1
    def sec():
        global count
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
                count += 1
                return
    def thir():
        global count
        id_search = int(input("Введите номер машины: "))
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
    def fourth():
        global count
        id_delete = int(input("Введите ID машины, которую требуется удалить "))
        for i in Marigold_data:
            if id_delete == i['id']:
                Marigold_data.remove(i)
                with open("Marigold.json", 'w', encoding='utf-8') as output_file:
                    json.dump(Marigold_data, output_file, ensure_ascii=False, indent=2)
                print("Машина удалена.")
                count += 1
    def fifth():
        global end
        print(f"Программа завершила свою работу. Кол-во операций равно {count}.")
        end = False
    def menu():
        while end:
            print("""Выберите действие:
            1: Вывести все записи
            2: Вывести запись по полю
            3: Добавить запись 
            4: Удалить запись по полю
            5: Выйти из программы
            """)
            n = int(input("Введите номер: "))
            if n == 1:
                fir()
            elif n == 2:
                sec()
            elif n == 3:
                thir()
            elif n == 4: 
                fourth()
            elif n == 5:
                fifth()
            else:
                print("Введено некорректное число!")          

menu()