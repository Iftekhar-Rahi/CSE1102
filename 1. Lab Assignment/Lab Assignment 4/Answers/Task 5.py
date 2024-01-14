word=input()
for i in range(1,len(word)+1):
  for j in range(0,i):
    print(word[j],end="")
  print()