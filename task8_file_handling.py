file = open("introduction.txt", "w")
file.write("My name is Smita.\nI am studying BCA.\nI am learning Python for Data Analytics.")
file.close()

file = open("introduction.txt", "r")
print(file.read())
file.close()
