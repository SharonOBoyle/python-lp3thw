def fillArray(size, increment):
        i = 0
        numbers = []

        while i < size:
            print(f"At the top i is {i}")
            numbers.append(i)

            i = i + increment
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {i}")


        print("The numbers: ")

        for num in numbers:
            print(num)

def fillArrayFor(stop, step):
        #i = 0
        numbers = []

        for i in range(0, stop, step):
            print(f"At the top i is {i}")
            numbers.append(i)

            #i = i + step # no longer needed
            print(">>> for loop: increment, i", step, i)
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {i}")


        print("The numbers: ")

        for num in numbers:
            print(num)


size = int(input("How many numbers do you want in the array? >>> "))
inc = int(input("What increment? >>> "))
fillArrayFor(size, inc)
