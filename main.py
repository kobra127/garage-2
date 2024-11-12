from operator import index
import sys
__name__ ="__main__"
UserCar=[]
Cars=[]
with open('UserCar.txt','r',encoding='utf=8') as f:
    with open('kolcars.txt','r') as file:
        I=file.readlines()
        I=I[0]
        I=int(I)
        for a in range(0, I):
            for b in range(0,5):
                y = f.readline()
                y = y.rstrip('\n')
                UserCar.append(y)
                if UserCar[0] == '':
                    UserCar = []
    with open('UserCar.txt','w',encoding='utf=8') as f:
        pass
with open('cars.txt','r') as f:
    v=len(UserCar)
    v=v//5
    for a in range(0,v+1):
        y=f.readline()
        y=y.rstrip('\n')
        Cars.append(y)
    Cars.pop(-1)
# N=1
# if N !=1:
#       UserCar = ['Ferrari California', 'Ferrari', 'красный', 'V8 - автоматическая', 'светодиодные (LED)']
#       Cars=['Ferrari California']
if Cars[0]=='':
    Cars=[]
car = 0
company = 1
colour = 2
box = 3
headlights = 4
x = 0
f = 0
while x!=1:
    Biblioteka = [UserCar]
    print('если вы хотите узнать х-ки машины, введите её нaзвание')
    print(Cars)
    print('если вы хотите добавить свою напишите add')
    print('если вы хотите удалить данные машины, напишите: del')
    print('что бы выйти напишите end')
    name=input()
    # завершение программы и сохранение
    if name =='end':
        s=len(Cars)
        with open('kolcars.txt','w') as f:
            f.write(str(s))
        g=len(UserCar)
        print(g)
        if g==0:
            print('завершение программы....')
            break
        print('завершение программы....')
        for n in range(0,g):
            l = UserCar[n]
            with open('UserCar.txt', 'a', encoding='utf-8') as file:
                file.write(l + '\n')
        with open('cars.txt', 'w', encoding='utf-8') as file:
            for Cars in Cars:
                file.write(Cars + '\n')
        break
    # удаляем машину
    elif name == 'del':
        print('напишите название машины из списка:')
        print(Cars)
        deleting = input()
        if deleting not in Cars:
            print('===============================')
            print('данные неверны')
            print('===============================')
            continue
        else:
            m=Cars.index(deleting)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            Cars.pop(m)
    # Добавляем информацию
    elif name=='add':
            print('введите название машины:')
            s = input()
            Cars.append(s)
            UserCar.append(s)
            print('введите компанию производителя машины:')
            s = input()
            UserCar.append(s)
            print('введите цвет машины:')
            s = input()
            UserCar.append(s)
            print('введите тип коробки передач машины:')
            s = input()
            UserCar.append(s)
            print('введите фары машины:')
            s = input()
            UserCar.append(s)
            continue
    # проверка на лоха
    if name=='del' or name=='add':
        continue
    if not (name in Cars):
        print('==============================')
        print('данные неверны')
        print('==============================')
        continue
    a = Cars.index(name)
    # информация о тачках
    print("============================================================================================")
    print('название:', UserCar[a * 5])
    print('компания:', UserCar[a * 5 + 1])
    print('цвет:', UserCar[a * 5 + 2])
    print('тип передач:', UserCar[a * 5 + 3])
    print('фары:', UserCar[a * 5 + 4])
    print("============================================================================================")
    print('введите что угодно, чтобы вернуться в меню.')
    h = input()
if __name__ == "__main__":
    main()
