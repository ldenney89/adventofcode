input = []
with open('input.txt','r') as fr:
  input = fr.readlines()

input = [int(x.strip()) for x in input]

print(input)

def fix_expense_report(lst):
  for x in range(len(lst)-3):
    for y in range(len(lst)-2):
      for z in range(len(lst)-1):
        if (lst[x]+lst[y]+ lst[z])== 2020:
          return lst[x]*lst[y]*lst[z], lst[x], lst[y], lst[z]

a, b, c, d = fix_expense_report(input)
print(a)
print(b)
print(c)
print(d)