password = 'Your password'

def ask_passsword():
    a = input()
    if a == 'Your password':
        print(password)
for i in reversed(range(3)):
    a = input("Enter the password: ")
    if a == 'Your password':
        print("Password accepted ")
        break
else:
    print("Access denied ")
