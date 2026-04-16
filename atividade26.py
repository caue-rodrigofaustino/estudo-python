import os

arquivo1 = open("dados.txt",  "w", encoding="utf-8")

print(os.path.abspath(arquivo1.name))

arquivo1.write("OLA MUNDO!")

print(os.path.realpath(arquivo1.name))

print(arquivo1)

arquivo1.close()