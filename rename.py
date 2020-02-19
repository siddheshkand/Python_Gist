import os
import re
path = "PATH"

for root,dir,file in os.walk(path):
    for d in dir:
        print(d)
        # print()
        files = os.listdir(os.path.join(root,d))
        for file in files:
            print('\t'+root+'\\'+d+'\\'+file)
            print('\t'+root+'\\'+d+'\\'+re.search(r'\d+', d).group()+'_'+file)
            os.rename(root+'\\'+d+'\\'+file,root+'\\'+d+'\\'+re.search(r'\d+', d).group()+'_'+file)

