#enter expression function
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



#calculate new tableau values
def new_tableau_value_calc(old_tableau_pivot_column, new_tableau_pivot_row,old_tableau_value):
          new_tableau_value = -(old_tableau_pivot_column) * (new_tableau_pivot_row) + (old_tableau_value)
          return round(new_tableau_value,2)

#get the smallest value in the objective function
#if the smallest value is less than 0 return 1 i.e the function is not optimal
#is the smallest value is greater than 0 return -1
def is_optimal(tableau):
          smallest_value = min(tableau[-1])
          if(smallest_value < 0):                    
                    smallest_value_index = tableau[-1].index(smallest_value)
                    return smallest_value_index
          else:
                    return -1

#determine pivot row through division
# takes two parameters. 
#       1) optimal which identifies the optimal column
#       2) st_rows_minus_maximise which
#          is a list of the tableau excluding 
#          the row which has the objective function         
def determine_pivot_row(optimal, st_rows_minus_maximise):
          smallest_division = 1000000000
          z = 0
          for i in st_rows_minus_maximise:
                    value = i[-1]/i[optimal]
                    if(value < smallest_division):
                              smallest_division = value
                              chosen_index = z

                    z += 1
          return chosen_index

#This is the Simplex tableau function that takes a tableau as a parameter              
def Simplex(tableau, w):
          #new tableau is where the new tableau at end of this function will be stored
          #start by copying and pasting the tableau in new tableau
          new_tableau = tableau.copy()

          #call the is_optimal function.
          #EITHER 
          #         index position e.g (0, 1, 2) of column 
          #         which has the least negative value
          #         (index of a list position can never be a negative ) 
          #OR 
          #         -1 is returned and stored in the optimal variable
          optimal = is_optimal(tableau)

          #if optimal == -1, the solution had no negatives in its objective function
          # it is optimal 
          if optimal == -1:
                    print("The solution is optimal")
                    return -1
          #else
          else:
                    #a list of the pivot column stored in smallest_column
                    smallest_column = [i[optimal] for i in tableau]

                    st_rows_minus_maximise = []
                    for i in tableau:
                              if(i == tableau[-1]):
                                        continue
                              st_rows_minus_maximise.append(i) 
                    chosen_row = determine_pivot_row(optimal,st_rows_minus_maximise)
                    smallest_value = tableau[chosen_row][optimal]

                    #----FORMULATING THE NEW TABLEAU------------#
                    
                    z = 0
                    for i in new_tableau[chosen_row]:
                              i = i / smallest_value
                              new_tableau[chosen_row][z] = i
                              z += 1
                    
                    z = 0
                    for i in new_tableau:
                              if (z == chosen_row):
                                        z = z + 1
                                        continue
                              x = 0
                              for k in new_tableau[z]:
                                        new_tableau[z][x] = new_tableau_value_calc(smallest_column[z], new_tableau[chosen_row][x],tableau[z][x])
                                        x += 1 
                              z = z + 1
                    print("\n")
                    print("step[" + str(w) + "]")
                    print(new_tableau)
                    return 1
          

tableau = []

print("\n#--------WELCOME TO THE SIMPLEX CALCULATOR-----------#\n")
print("Instructions")
print("============")
print("1. You may enter as many st expressions as you wish")
print("2. When asked in the program, y = yes n = no to enter st expressions(constraints)")
print("3. You will be prompted to enter the objective expression last")

print("\n")

b_count = 1
a_count = 1
c_count = 1 

while True:
          try: 
                    val = input("Do you want to add another st expression? [y or n]: ")
		
                    if(val == 'n'):
                              w = 'c'
                              print("\nAdd the objective expression: ")
                              enter_expression(tableau, w)
                              break
                    else:
                              w = 'a'
                              enter_expression(tableau, w)
          except:
                    print("\n*****WRONG INPUT*****")
                    print("      start afresh    \n")
                    b_count = 1
                    a_count = 1
                    c_count = 1 
                    tableau = []

                    
w = 1
value = 1
while(value == 1): 
                   
          value = Simplex(tableau, w)
          w += 1

          
          

