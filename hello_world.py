print ('hello World!')

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("This is not a valid age.")
        continue
    else:
        break


print(f"You are {age} years old")
