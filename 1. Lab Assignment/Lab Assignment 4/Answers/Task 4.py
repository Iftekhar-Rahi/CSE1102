word=input()
if word[len(word)-2:len(word)]=="er":
    print(word[0:len(word)-2]+"est")
elif word[len(word)-3:len(word)]=="est":
    print(word)
elif len(word)>3:
    print(word+"er")
elif len(word)<4:
    print(word)