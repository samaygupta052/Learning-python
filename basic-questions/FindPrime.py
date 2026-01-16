# what is a prime number?
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.   

while True:
    num = int(input("Enter a number: "))

    if num <=1:
         print(f"{num} is not a prime number.")
    else:
        for i in range(2, num):
          if num % i ==0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number.")

    
    choice = input("Do you want to check another number? (yes/no): ").lower()
    if choice != "yes":
        print("Program ended.")
        break