
while  True:
    item_name = input("item  : ")
    quatity = input("quatity : ")
   unit_price = input("unit price : ")

   amount = quatity*unit_price 
   total_bill += amount
   more_items = input("do you hav more items y/n")    
   
    if more_items ==" y":
        continue
    else:
        break

     

