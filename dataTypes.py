# ! Non-Liner Data Structures
# * Binary Tree − It is a data structure where each data element can be connected to maximum two other data elements and it starts with a root node.
# * Heap − It is a special case of Tree data structure where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes.
# * Hash Table − It is a data structure which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element.
# * Graph − It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.

# ! Python Specific Data Structures
# * List − It is similar to array with the exception that the data elements can be of different data types. You can have both numeric and string data in a python list. (kind of like an untyped array)
# * Tuple − Tuples are similar to lists but they are immutable which means the values in a tuple cannot be modified they can only be read.
# * Dictionary − The dictionary contains Key-value pairs as its data elements. (Object)

################# Lists or Arrays (in js)

# [20,32,21,19,3] == array('i', [10, 20, 30, 40, 50])
# arrays are 0 indexed

array1 = [10, 20, 30, 40, 50]

# array1.insert(0, 44)
# array1.remove(20)
# print(array1.index(30))

# mutate an array
# array1[3] = 400

# * common way to iterate:
# for x in array1:
#     print(x)

# !!!! NOTE: for transforming a list of dictionaries, you have two options: 
arr = [
    {"name": "gabe", "age": "4", "job": "dev", "salary": "64000000000000"},
    {"name": "dave", "age": "3", "job": "sad", "salary": "64000000000000"},
    {"name": "mave", "age": "10", "job": "mad", "salary": "332123"},
    {"name": "flave", "age": "24", "job": "dev", "salary": "64000000000000"},
    {"name": "rave", "age": "34", "job": "flad", "salary": "64000000000000"},
    {"name": "pave", "age": "34", "job": "dev", "salary": "64000000000000"},
    {"name": "tame", "age": "34", "job": "map", "salary": "64000000000000"},
    {"name": "grape", "age": "33", "job": "dev", "salary": "64000000000000"},
]

# *** OPTION 1: Loop through the items and use whatever property as the nested dictionary's key:
obj = {};

for item in arr:
    name = item.pop('name')
    obj[name] = item
    print(obj)

obj["gabe"]["age"]

#  prints:
# {
#   "gabe": {
#     "age": "4",
#     "job": "dev",
#     "salary": "64000000000000"
#   },
#   "dave": {
#     "age": "3",
#     "job": "sad",
#     "salary": "64000000000000"
#   },
#   "mave": {
#     "age": "10",
#     "job": "mad",
#     "salary": "332123"
#   },
#   "flave": {
#     "age": "24",
#     "job": "dev",
#     "salary": "64000000000000"
#   },
#   "rave": {
#     "age": "34",
#     "job": "flad",
#     "salary": "64000000000000"
#   },
#   "pave": {
#     "age": "34",
#     "job": "dev",
#     "salary": "64000000000000"
#   },
#   "tame": {
#     "age": "34",
#     "job": "map",
#     "salary": "64000000000000"
#   },
#   "grape": {
#     "age": "33",
#     "job": "dev",
#     "salary": "64000000000000"
#   }
# }

# **** Option 2:
# object_dict = {id(x): x for x in arr}

# id() generates a guaranteed unique id for an object

# prints: 
# {
#   "4435303488": {
#     "name": "gabe",
#     "age": "4",
#     "job": "dev",
#     "salary": "64000000000000"
#   },
#   "4435303808": {
#     "name": "dave",
#     "age": "3",
#     "job": "sad",
#     "salary": "64000000000000"
#   },
#   "4431140608": {
#     "name": "mave",
#     "age": "10",
#     "job": "mad",
#     "salary": "332123"
#   },
#   "4435302784": {
#     "name": "flave",
#     "age": "24",
#     "job": "dev",
#     "salary": "64000000000000"
#   },
#   "4429887488": {
#     "name": "rave",
#     "age": "34",
#     "job": "flad",
#     "salary": "64000000000000"
#   },
#   "4435304448": {
#     "name": "pave",
#     "age": "34",
#     "job": "dev",
#     "salary": "64000000000000"
#   },
#   "4435305408": {
#     "name": "tame",
#     "age": "34",
#     "job": "map",
#     "salary": "64000000000000"
#   },
#   "4435304128": {
#     "name": "grape",
#     "age": "33",
#     "job": "dev",
#     "salary": "64000000000000"
#   }
# }