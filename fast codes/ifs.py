# aprogram to compute wage 

# user input
employee_name  = str (input("Enter employee_name:"))
hours_worked   = int (input("Enter hours_worked:"))

# computation 
fixed_rate = 30000 
wage = (hours_worked*fixed_rate )

if wage>= 500000:
    print("compulsory tax payment")
else:
    print("tax exmpeted")
# output
print(f"wage: {wage}")