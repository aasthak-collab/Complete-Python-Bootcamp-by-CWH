#adding hometown address of john doe by using append to a file in python
f =open("John Doe.txt","a")
string = '''
He lived in NYC
'''
f.write(string)
f.close()