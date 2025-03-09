
stu_dict = {"name":"sam","grade":10,"age":16}

print(stu_dict)
print(stu_dict["name"])
print(stu_dict["grade"])
print(stu_dict["age"])

stu_dict["age"] = 17
print(stu_dict)

stu_dict.pop("grade")
print(stu_dict)

stu_dict["gender"] = "Male"
print(stu_dict)

stu_dict.clear()
print(stu_dict)