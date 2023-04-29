password = 'Собачий клюв'

def ask_passsword():
    a = input()
    if a == 'Собачий клюв':
        print(password)
for i in reversed(range(3)):
    a = input("Введите пароль: ")
    if a == 'Собачий клюв':
        print("Пароль принят ")
        break
else:
    print("В доступе отказано ")
