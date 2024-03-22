# aprogram to show and compute students assessments

count = 0
students = 5
number_of_subjects = 3

#user input
while count < students:
    print ("\n\t\tStudents Assesment")
    #user input
    name = input("Enter Name ")
    test1= int(input("Enter Math scores :"))
    test2 = int(input("Enter English scores :"))
    test3 = int(input("Enter PE scores :"))

 # computation of Total and Average 
    Total = test1 + test2 +test3
    Average = Total/number_of_subjects 

print(f" {Name} Your total is , {Total} and Average is {Average}") 

count += 1
