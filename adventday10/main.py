input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_input = input.split("\n")

nums = [int(x) for x in lst_input]

nums.sort()

count1=0
count3=0
for x in range(len(nums)-2):
  diff = nums[x+1] - nums[x]
  if diff == 1:
    count1+=1
  elif diff == 3:
    count3+=1
print(count1*count3)
