qt={ }
amount=0
pr={1:30,2:75,3:99,4:50,5:15}
nm={1:'Toothpaste',2:'Shampoo',3:'Cooking Oil',4:'Sugar',5:'Salt'}
print("                                    MENU				")
print("======================================================================")
print("Product No                 |       Product Name         |       Price")
print("1                          |       Toothpaste           |       30")
print("2                          |       Shampoo              |       75")
print("3                          |       Cooking Oil          |       99")
print("4                          |       Sugar                |       50")
print("5                          |       Salt                 |       15")
print("======================================================================")
while(True):
    i=int(input("Enter your Product No:"))
    qt[i]=int(input("Enter quantity:"))
    amount=amount+(qt[i]*pr[i])
    print("Do you wish to add more entry?..(Y,N)")
    en=input()
    if(en=='N' or en=='n'):
        break
print("----------------------------------------------------------------------------------")
print("                        		    INVOICE                                   ")
print("----------------------------------------------------------------------------------")
i=0
print("Product No                |Price       |Quantity        |Product Name")
for i in qt:
    print(i,"                        |",pr[i],"        |",qt[i],"		|",nm[i])
print("Total amount:",amount)
w=input()
