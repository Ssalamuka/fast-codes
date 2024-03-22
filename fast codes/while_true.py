# aprogram to show and compute students assessments

students = 5
number_of_subjects = 3

#user input
while True:
    print ("\n\t\tStudents Assesment")
    #user input
    name = input("Enter name ")
    test1= int(input("Enter Math scores :"))
    test2 = int(input("Enter English scores :"))
    test3 = int(input("Enter PE scores :"))

    Total = test1 + test2 +test3
    Average = Total/number_of_subjects 
    print(f"\n {name} \n Your total is , {Total} and Average is \n{Average}")
    more_students = input("To  Enter more Students yes/no : ")

    if more_students == "yes":
        continue
    else:
        break   


