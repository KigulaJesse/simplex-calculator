
tableau = [
          [0.0, -2.0, 1.0, 1.0, -1.0, 0.0, 2.0],
          [1.0,  5.0, 1.0, 0.0, 1.0, 0.0, 8.0],
          [0.0, 30.0, 1.0, 0.0, 8.0, 1.0, 64.0]
]

cols = []
for x in range(0,len(tableau[0]),1):
         cols.append([i[x] for i in tableau])

solution = []

z = 0
for i in cols:
          if z == (len(cols)-1):
                    break
          print(i)
          y = 0
          count_0s = 0
          count_1s = 0
          for p in i:
                    
                    if p == 1:
                              print(p)
                              print(y)
                              col = y
                              count_1s += 1
                    if p == 0:
                              count_0s += 1
                    y += 1

          z += 1

          if (count_0s == (len(i) - 1)) & (count_1s == 1):
                    solution.append(cols[-1][col])
          else:
                    solution.append(0)

#solution.append(cols[-1][-1])
print("\n")
print(solution)

g = 1
k = 1
                    
          
for f in solution:
          if g <= 3:          
                    print("ci"+str(g)+" = " + str(f))
                    g += 1
          elif g < len(solution):
                    print("s"+str(k)+" = " + str(f))
                    k += 1
                    g += 1
          else:
                    print("z = " + str(f))
                    
          
