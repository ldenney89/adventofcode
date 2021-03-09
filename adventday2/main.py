input = []
with open('input.txt','r') as fr:
  input = fr.readlines()

lst = [item.strip().split(":") for item in input]
#print(len(lst))

#print(dic)
countvalid = []
for i in lst:
  temp = i[0].split("-")
  temp2 = temp[1].split(" ")
  temp3 = (int(temp[0]), int(temp2[0]), temp2[1])
  print(temp3)
  print(i)
  mi, ma, st = temp3
  #print(temp3)
  #if i[1].count(temp3[2]) >= temp3[0] and i[1].count(temp3[2]) <= temp3[1]:
  if i[1][mi] == st and not(i[1][ma] == st):
    countvalid.append(1)
  elif not(i[1][mi] == st) and i[1][ma] == st:
    countvalid.append(1)
  else:
    countvalid.append(0)
print(sum(countvalid))
print(len(countvalid))

