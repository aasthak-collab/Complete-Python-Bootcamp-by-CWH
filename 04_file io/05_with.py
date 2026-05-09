#with provides more cleaner way to work with files(also known as context manager)
with open("aastha.txt", "r") as f:
    content = f.read()
    print(content)
    #no need to use f.close() because we have used with syntax and in this the file is closed by default 