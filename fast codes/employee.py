# programe to compute employee bouns

# given data 
bonus = 0
# computation 
if years >=10:
    years = int(input("Enter Years of Service"))
    salary= float(input("Enter Salary"))
    percentage = (years*0.1)
    print(f"Bonus  :{percentage}")
 elif years >= 6:
       percentage1  = (years*0.08)
    elif years <6:
        percentage2  = (years*0.05)
    print(f"Net bonus: {years})S