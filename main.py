student = ("Michael", "20", "excellent student")

print(student.count("Michael"))
print(student.index("excellent student"))

for x in student:
    print(x)

if "Michael" in student:
    print("Michael is here!")