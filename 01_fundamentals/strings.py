# # strings in python: string can be written with single,double,triple quotes(and triple quotes are used for multi line strings)
# #indexing and strings
# name = "HENRY"
# print(name[0])
# print(name[1])
# print(name[2])
# #the output will be H,E,N

# #String slicing
name = "Henry0123456789"
# print(name[0:2]0)#this acts like range which goes from 0 to 2-1
# print(name[2:-1])#same as name[2:4]
# #STEP SLICING = this step parameter defines the interval of slicing
# #print(name[0:10:n])# skip n-1 characters
# print(name[0:10:1])# skip 0 characters
# print(name[0:10:2])# skip 1 characters
# print(name[0:10:3])# skip 2 characters
# print(name[:4])#replaces the first empty number with  0
# print(name[4:])#replaces the second  empty number with the length

#STRING METHODS AND FUNCTIONS:
#Changing case:
s = "hello world"
print(s.upper()) #output : "HELLO WORLD"
print(s.lower()) #output: "hello world"
print(s.title()) #output: "Hello World"#1st letter of every word will be capital
print(s.capitalize()) # output: "Hello world"