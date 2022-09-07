import re
def find_sum(str1):
    sum=0
    result= [int(d)for d in re.findall('\d+', str1)]
    for i in  result:
        if(i<0):
            return "negative not allowed"
#             break
        else:
            sum+=i
    return sum
find_sum('6+1-5*4')