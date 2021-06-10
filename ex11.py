string = input("Tell me something: ")
print(f"You told me: \"{string}\"")

numF = float(input("Enter float value: "))
numI = int(input("Enter int value: "))
result = numF * numI
print(f"Result of {numF} * {numI} = ", result)

print("How old are you?", end=' ')
age = int(input())
print(">>>> age = ", repr(age))
age_next_year = age + 1
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("Type of \"age\" is: ", type(age))
print("Type of \"weight\" is ", type(weight))
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print(f"So you will be {age_next_year} on your next birthday.")

name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

print("\n")
print("Printing Employee Details")
print("Name", "\tSalary", "\tCompany")
print(f"{name}\t {salary}\t {company}")
