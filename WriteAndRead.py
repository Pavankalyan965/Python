f1 = open('world cities','w')
f1.write('Mumbai,India\n')
f1.write('Chicago,USA\n')
f1.write('Paris,France\n')
f1.close()

f1 = open('world cities','r')
print(f1.read())