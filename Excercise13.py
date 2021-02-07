def merge(dict1,dict2):
    return (dict2.update(dict1))
dict1={'a':10,'b':8}
dict2={'x':17,'y':20}
print(merge(dict1,dict2))
print(dict2)
