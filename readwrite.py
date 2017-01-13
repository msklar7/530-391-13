def read(): 
  f = open("input", 'r')

  #read a
  line = f.readline()
  split = line.split()
  a =float(split[2])

  #read b
  line = f.readline()
  split = line.split()
  b = float(split[2])

  #readc
  line = f.readline()
  split = line.split()
  c = float(split[2])

  print(a, b, c)

  #clean up
  f.close()

  #return a, b, c
  return[a, b, c]

