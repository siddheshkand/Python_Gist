# [0-9]\d+ [A-Z]\w+ [A-Z]\w+ [A-Z]\w+
import re

file = open('10070.txt',mode='r')
text = file.read()
# print(text)
regex = r"[0-9]\d+ [A-Z]\w+ [A-Z]\w+ [A-Z]\w+" 
matches = re.finditer(regex, text, re.MULTILINE)
 
for matchNum, match in enumerate(matches, start=1):
    # print(matchNum)
    # print(match.group()[-5:])
    print(match.group())
 