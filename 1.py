tableau = [
          [0.0, -2.0, 1.0, 1.0, -1.0, 0.0, 2.0],
          [1.0,  5.0, 1.0, 0.0, 1.0, 0.0, 8.0],
          [0.0, 30.0, 1.0, 0.0, 8.0, 1.0, 64.0]
]

s = [[str(e) for e in row] for row in tableau]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print ("\n".join(table))