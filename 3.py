tableau = [
          [6, 8, 1, 1, 0, 100],
          [4, 3, -2, 0, 1,90],
]

last = tableau[0][-1]
tableau[0][-1] = (0)
tableau[0].append(last)
print(tableau)