tableau = []

print("\n#--------WELCOME TO THE SIMPLEX CALCULATOR-----------#\n")
print("Instructions")
print("============")
print("1. The  LAST expression entered is the objective expression")
print("2. You may enter as many expressions as you wish")
print("3. When asked in the program, y = yes n = no")
print("\n")

def enter_expression(tableau, w):
          col = []
          global a_count
          global b_count
          global c_count

          

          for i in range(1,4,1):
                    if w == 'a':
                              a = input("Input "+ w +str(a_count)+" = ")
                              a_count += 1
                    elif ((w == 'c') & (c_count == 1)) :
                              a = input("Input "+ w + "i" +" = ")
                              c_count += 1
                    else:
                              a = input("Input "+ w + "i" + str(c_count)+" = ")
                              c_count += 1
                    col.append(int(a))
                    
          if b_count == 1:
                    b = input("Input bi = ")
                    b_count += 1

          else:
                    b = input("Input bi"+str(b_count)+" = ")
                    b_count += 1
          
          if len(tableau) >= 1:
                    g = 0
                    for i in tableau:
                              last = tableau[g][-1]
                              tableau[g][-1] = (0)
                              tableau[g].append(last)
                              g += 1
                              col.append(0)
                    col.append(1)
                    col.append(int(b))
                    tableau.append(col)

          else: 
                    col.append(1)
                    col.append(int(b))
                    tableau.append(col)

b_count = 1
a_count = 1
c_count = 1 

while True:
          try: 
                    val = input("Add another st expression [y or n]: ")
		
                    if(val == 'n'):
                              w = 'c'
                              val = input("Add objective expression [y or n]: ")
                              enter_expression(tableau, w)
                              break
                    else:
                              w = 'a'
                              enter_expression(tableau, w)
          except ValueError as e:
                    print("\n*****WRONG INPUT*****")
                    print("      start afresh    \n")
                    b_count = 1
                    a_count = 1
                    c_count = 1 
                    tableau = []


                    
print (tableau)
