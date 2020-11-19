number = int(input("Prime numbers between 2 and "))
for num in range(2,number + 1):
       if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                     break
            else:
                print(num)