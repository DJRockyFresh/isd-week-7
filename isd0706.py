s1 = input("Enter a short sentence: ")
s2 = input("Enter another short sentence: ")

print(s1 + s2)
s = [s1, s2]
s = [word for line in s for word in line.split()]
print(s)

s.sort() 
print("Sorted:", s)

slength = len(s)
print("Word count:", slength)

#d = {"s": "sentences"}


d = {}
for i in range (len(s)):
    d[i] = s[i]

print(d)    
