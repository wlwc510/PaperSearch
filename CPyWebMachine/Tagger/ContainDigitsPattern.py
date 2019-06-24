#coding:utf-8
import re

stritem = 'Structurally, these [6] dimers possess congested frameworks of at least eight rings decorated by more than 11 stereogenic centers.'
pattern = re.compile('\[.*\]')
match = pattern.findall(stritem)
for matchi in match:
    matchi=matchi.replace('[','')
    matchi=matchi.replace(']','')
    # test=int(matchi)
    # print(test)
    # test="4"
    if(matchi.isdigit())
        return true
    try:
        test=str(int(matchi))
        # print(test.isdigit())
    except :
        print("not references")

    # print(test.isdigit())
    # pattern = re.compile('\d+')
    # if pattern.findall(matchi):
    #     print("find one")
    #     break
