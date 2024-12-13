base_salary=float(input("enter the  base salary"))
if(base_salary<10000) :
     hra=(67/100) * base_salary
     da=(73/100) * base_salary

elif( base_salary<20000):
    hra = (69 / 100) * base_salary
    da = (76 / 100) * base_salary
else:
    hra = (73 / 100) * base_salary
    da = (89 / 100) * base_salary
total_salary = base_salary + hra + da
print("total gross salary:",total_salary)



