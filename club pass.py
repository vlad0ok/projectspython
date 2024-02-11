name = input("Enter your name: ")
age = int(input("Enter your age: "))
reserve = input("Did you reserve entry?(yes/no): ")
res_ch = False
if reserve == 'yes':
    res_ch = True

if age >= 18 and res_ch == True:
    print(f"Entry allowed, dear {name}")
else:
    print(f"Entry NOT allowed, dear {name}")