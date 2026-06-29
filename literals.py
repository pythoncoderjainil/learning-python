
a = 0b1010 #binary literals
b = 100 #decimal literals
c = 0o310 #octal literals
d = 0x12c #hexadecimal literals

#Float literals
float_1 = 10.5
float_2 = 15e2
float_3 = 15e-3

#complex literals
x= 3.14j

print(a,b,c,d)
print(float_1,float_2,float_3)
print(x, x.imag, x.real)

#string literals
string = 'this is python'
strings= "THIS IS MY PYTHON CODE"
char = 'c'
multiline_str= """this is the multiline string with more than 1 line code"""
unicode = u"\u0001f600\u0001f606"
raw_str = r"raw \n string"
print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


#boolean literal
a= True + 4
b= False + 10
print("a:",a)
print("b:",b)

#Special literals
a= None
print(a) #this will print None because it is a special literal in python which is used to represent the null value or no value at all.
