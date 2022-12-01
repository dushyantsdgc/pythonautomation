
f = open("demo_test_File1.txt2", 'w')
f.write("This time try to append to file")
f.close()

f = open("demo_test_File.txt", 'r')
print(f.read(10))
print(f.read())
f.close()

print(f. read(10))
print(f. read())