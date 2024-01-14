word=input()
flag=True
for i in range(0,len(word)):
  if word[i]!="0" and word[i]!="1":
    flag=False
    break
if flag==True:
  print("Binary Number")
elif flag==False:
  print("Not a binary Number")