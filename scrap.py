import re
import statistics
file = open('14450.txt',mode='r')
text = file.read()
# print(text)
regex = r"SGPA : \(1\) [0-9]+.[0-9]+" 
matches = re.finditer(regex, text, re.MULTILINE)

print(matches)
a = []
for matchNum, match in enumerate(matches, start=1):
    # print(matchNum)
    # print(match.group()[-5:])
    a.append(float(match.group()[-5:]))

a.sort()
a.reverse()
for val in a :
    print(val)

print(sum(a) / len(a))
print(max(set(a), key=a.count))
print(statistics.median(a))     