'''
a = "competitive programming"

print(a)
print(type(a))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.count("e"))
print(a.endswith("ing"))
print(a.endswith("ps"))
print(a.find("o"))
print(a.find("i",9))
print(a.replace("o",'0'))

'''

a = "g.niruthian"

print(a.isupper())
print(a.islower())

b = "NIRU 15"

print(b.isalpha())
print(b.isnumeric())
print(b.isalnum())

n = "G.Niruthian\nis\nthe\nbest\ncompetitive programmer"
print(n)
print(n.splitlines())
print(n.splitlines(True))
print((n.split(" ")))
n = "G.Niruthian, is the, best, programmer, in the world."
print(n.split(","))
n= "        NIRU           "
print(len(n))
print(len(n.strip()))
print(len(n.lstrip()))
print(len(n.rstrip()))
s = '1-01-2023'
print(s.partition('-'))