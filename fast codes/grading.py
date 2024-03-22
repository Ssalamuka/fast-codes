cgpa=float(input("Enter CGPA : "))

cgpa_class="" 

if cgpa_class<=1.9:
  cgpa = "Fail"
elif cgpa_class<=2.4:
    cgpa="pass"
elif cgpa_class<=3.5:
    cgpa="second class lower"
elif cgpa_class<=4.4:
    cgpa="second class upper"    
elif cgpa_class<=5.0:
    cgpa="first class"    
else:
    print(" CGPA NOT ALLOWED ")    

print(f"\ncgpa: {cgpa}\tclass:{cgpa_class}\n")