
sal = float(input("Enter the salary: "))
bill1 = float(input("Enter the bill 1: "))
bill2 = float(input("Enter the bill 2: "))
bill3 = float(input("Enter the bill 3: "))


sum_bills = bill1 + bill2 + bill3
print("Sum of bills: " + str(sum_bills))
percentage = (sum_bills / sal) * 100

print("Percentage of usage of salary: "+str(percentage))
