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


size = int(input("How many numbers do you want in the array? >>> "))
inc = int(input("What increment? >>> "))
fillArray(size, inc)
