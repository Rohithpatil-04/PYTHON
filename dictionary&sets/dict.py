# are used to store data values in key value pairs


# they are unordered ,mutable ,dont allow duplicate keys


# info = {

#       "key": "value",
#       "name":"apna college",
#       "subjects": ["python","cpp","java"],
#       "topics": ("dict","sets"),
#       "learning": "coding",
#       "age" : 35,
#       "is_adult" :True,
#       "marks" : 94.5


# }

# print(info)
# print(type(info))

# info["name"] ="shradha"

# info["surname"] ="khapra"

# print(info)





#nested dict


# student = {
#     "name": "annup kumar",
#     "subject" : {
#         "phy":90,
#         "chem":98,
#         "math":95
#     }
# }

# print(student["subject"] ["chem"])





#methods


student = {
    "name": "annup kumar",
    "subject" : {
        "phy":90,
        "chem":98,
        "math":95
    }
}


# print(len(student))

# print(student.keys())

# print(student.values())

# print(student.items())


# print (list(student.items()))


# pairs=list(student.items())
# print(pairs[0])


# print(student["name"])
# print(student.get("name"))


student.update({"city": "delhi"})
print(student)