input = []

with open('input.txt','r') as fr:
  input = fr.read()

lst_input = input.split("\n")

nums = [int(x) for x in lst_input]

nums.append(0)
nums.sort()
nums.append(nums[-1]+3)


def countdiffs(nums):
  count1=0
  count3=0
  for x in range(0,len(nums)-1):
    diff = nums[x+1] - nums[x]
    if diff == 1:
      count1+=1
    elif diff == 3:
      count3+=1
    else:
      raise Exception
  print(count1*count3)


