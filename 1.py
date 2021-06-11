#calculate values
def new_tableau_value_calc(old_tableau_pivot_column, new_tableau_pivot_row,old_tableau_value):
          new_tableau_value = -(old_tableau_pivot_column) * (new_tableau_pivot_row) + (old_tableau_value)
          return new_tableau_value

#check if optimal return column of least
def is_optimal(m):
          smallest_value = min(m)
          if(smallest_value < 0):                    
                    smallest_value_index = m.index(smallest_value)
                    return smallest_value_index
          else:
                    return False

#determine pivot row through division
def determine_pivot_row(smallest_column,beta_column_minus_optimal):
          smallest_division = 1000000000
          for i in range(0,len(smallest_column),1):
                    for j in range(0,len(beta_column_minus_optimal),1):
                              if(i == j):
                                        value = beta_column_minus_optimal[j]/smallest_column[i]
                                        if(value < smallest_division):
                                                  smallest_division = value
                                                  chosen_index = i 
          return chosen_index



#st
a = [[1, 3, 2, 1, 0, 0, 10],
     [1, 5, 1, 0, 1, 0, 8]
     [-8, -10, -7, 0, 0, 1, 0]
]
    
#maximise function
m = [-8, -10, -7, 0, 0, 1]
#beta column
b = [10, 8, 0]


optimal = is_optimal(m)
beta_column_minus_optimal = []

if optimal == False:
          print("The solution is optimal")
else:
          smallest_column = [i[optimal] for i in a]

          z = 0
          for i in b:
                    if (z == len(smallest_column)):
                              break
                    beta_column_minus_optimal.append(i)
                    z += 1
          
          chosen_row = determine_pivot_row(smallest_column,beta_column_minus_optimal)
          smallest_value = a[chosen_row][optimal]

          print(smallest_value)
          

          #-------------COME UP WITH NEW A ---------------#
          z = 0
          new_a = a.copy()
          for i in new_a[chosen_row]:
                    i = i /smallest_value
                    new_a[chosen_row][z] = i
                    z += 1

          z = 0
          for i in new_a:
                    if (z == chosen_row):
                              continue
                    x = 0
                    for k in new_a[z]:
                              new_a[z][x] = new_tableau_value_calc(smallest_column[z], new_a[chosen_row][x],a[z][x])
                              x += 1     
                    z += 1
          #-------------------END OF NEW A---------------#

          #---------------COME UP WITH NEW M-------------#
          z = 0
          new_m = m.copy()
          for i in new_m:
                    new_m[z] = new_tableau_value_calc(m[optimal], new_a[chosen_row][z],m[z])
                    z += 1
          #---------------END OF NEW M-------------------#

          #-------------COME UP WITH NEW B---------------#
          z = 0
          new_b = b.copy()
          for i in new_b:
                    #new_b[z] = new_tableau_value_calc(m[optimal], new_a[chosen_row][z],m[z])
                    z += 1
                    
          # --------------END OF NEW B-------------------# 
                    

          
          

                    