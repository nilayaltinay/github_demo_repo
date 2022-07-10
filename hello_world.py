print ('hello World!')


name = input("Enter your First name: ")

surname = input("Enter your Surname: ")



while True:
    try:
        age = int(input("Enter your age please: "))
    except ValueError:
        print("This is not a valid age.")
        continue
    else:
        break
        


print(f"Hello {name}" , f"{surname}" , f"You are {age} years old" )
