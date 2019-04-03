from sys import argv

script, filename = argv
txt = open(filename)
print("Here's your file %r" % filename)
# for line in txt.readlines():
#     print(line)
print(txt.read())
txt.close()