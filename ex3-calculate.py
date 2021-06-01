print("Before tax:")
print("Full pension is 2300.00 per month")
print("One year lose 4% means pension is", 2300.00 - 2300.00 * 4/100) #2208
print("Two years lose 8% means pension is", 2300.00 - 2300.00 * 8/100) #2116

print("After tax:")
print("Full pension less tax of 20% is", 2300 - 2300 * 20/100) #1840
print("One year pension after tax of 20% is", 2208 - 2208 * 20/100) #1766.40
print("Two year pension after tax of 20% is", 2116 - 2116 * 20/100) #1692.80

print("Net amount lost per annum for retiring early:")

print("One year early (next year)", (1840 - 1766.40) * 12)
print("Two years early (this year)", (1840 - 1692.80) * 12)
