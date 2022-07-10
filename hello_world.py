print ('hello World!')


while True:
    try:
        age = int(input("Enter your age please: "))
    except ValueError:
        print("This is not a valid age.")
        continue
    else:
        break
        
name = input("Enter your name: ")

print(f"Hello {name}" , f"You are {age} years old" )
