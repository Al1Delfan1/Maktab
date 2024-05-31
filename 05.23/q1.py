age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: "))

oldest_age = max(age1, age2, age3)
youngest_age = min(age1, age2, age3)

print("oldest: " + str(oldest_age))
print("youngest: " + str(youngest_age))