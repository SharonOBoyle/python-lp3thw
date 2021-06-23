def my_function(count_of_beers, count_of_pizzas):
    print(f"We have {count_of_beers} beers!")
    print(f"We have {count_of_pizzas} pizzas!")
    print("Let's have a party!\n")

# way 1
print("We can send values directly to the function")
my_function(30, 5)

# way 2
print("We can do some math when calling the function")
my_function(30 - 3, 5 * 2)

# way 3
print("We can define variables in our script and send them")
beers = 12
pizzas = 2
my_function(beers, pizzas)

# way 4
print("We can calulate some updated values and send them")
more_beers = beers + 10
more_pizzas = pizzas + 5
my_function(more_beers, more_pizzas)

# way 5
print("We can update values directly when we call the function")
my_function(beers + 50, pizzas + 10)

# way 6
print("We can ask the user to input values and send them")
user_beers = input("How many beers do we have? ")
user_pizzas = input("How many pizzas do we have? ")
my_function(user_beers, user_pizzas)

# way 7
print("We can ask the user for values when calling the function")
my_function(input("How many beers? "), input("How many pizzas? "))
