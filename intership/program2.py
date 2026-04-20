def is_anagram(s,t):
    if len(s)!=len(t):
        print("Not Anagram")
    else:
        if sorted(s)==sorted(t):
            print("Anagram")
        else:
            print("Not Anagram")
s=input("enter first string:")
t=input("enter second string:")
is_anagram(s,t)
