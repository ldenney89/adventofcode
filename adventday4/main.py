VALID1 = {'ecl','pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}
VALID2 = {'ecl','pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}

input = []
with open('input.txt','r') as fr:
  input = fr.read()

#print(input)

lst = input.split('\n\n')
#print(lst)

all_passports = []
for item in lst:
  temp = item.split("\n")
  #print(temp)
  spaces = " ".join(temp)
  #print(spaces)
  lst_passport = spaces.split(" ")
  #print(lst_passport)
  dic_passport = {item.split(':')[0]: item.split(":")[1] for item in lst_passport}
  print(dic_passport)
  all_passports.append(dic_passport)
#print(all_passports)
'''
validcount = 0
for item in all_passports:
  if VALID1 <= item.keys():
    validcount+=1
  elif VALID2 <= item.keys():
    validcount+=1

print(validcount)
'''
def birth_year(byr):
  if len(byr) > 4 or len(byr) < 4:
    return False
  if int(byr) < 1920 or int(byr) > 2002:
    return False
  return True

def issue_year(iyr):
  if len(iyr) > 4 or len(iyr) < 4:
    return False
  if int(iyr) < 2010 or int(iyr) > 2020:
    return False
  return True

def expiration_year(eyr):
  if len(eyr) > 4 or len(eyr) < 4:
    return False
  if int(eyr) < 2020 or int(eyr) > 2030:
    return False
  return True

def height(hgt):
  unit = hgt[-2:]
  value = int(hgt[:-2])
  if unit == 'cm':
    if value < 150 or value > 193:
      return False
    else: return True
  elif unit == 'in':
    if value < 59 or value > 76:
      return False
    else: return True 

def hair_color(hcl):
  if hcl[0] != '#':
    return False
  elif len(hcl[1:]) > 6:
    return False
  else:
    return True

def eye_color(ecl):
  if ecl in 'amb blu brn gry grn hzl oth':
    return True
  else:
    return False

def passport_id(pid):
  if(len(pid)== 9) and pid.isdigit():
    return True
  else:
    return False

def country_id(cid):
  return True
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

validcount = 0
for item in all_passports:
  try:
    if birth_year(item['byr']) and issue_year(item['iyr']) and expiration_year(item['eyr']) and height(item['hgt']) and hair_color(item['hcl']) and eye_color(item['ecl']) and passport_id(item['pid']):# and country_id(item['cid']):
      validcount+=1
  except Exception as e:
    print(e)
print(validcount)