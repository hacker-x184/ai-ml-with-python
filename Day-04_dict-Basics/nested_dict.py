student = {
    "name" : "Inzamam",
    "marks" : {
        "chem": 98,
        "maths":54,
        "phy":67,
    },
    "class": 12,
}
# this is the way of printing th evalue of the nested dictionary
print(student["marks"["maths"]])
# Some methods of dictionary
print(student.key())#they gve us the all the key dictionary
print(student.values())#they give us the all the value of the the dictionary
print(student.items())#they gve us the all the key and value dictionary
print(student.get())
print(student.update({"Nikename":"Anonnymous"}))