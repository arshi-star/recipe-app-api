from django.shortcuts import render

# Create your views here.

def remove_duplicates(rem_dup):
    remove_same = set()
    for unique in rem_dup:
        if unique not in remove_same:
            remove_same.add(unique)
    print(remove_same)        
    return remove_same

# obj = [1,2,1,3,3,2,4,8,9]
# obj_call=remove_duplicates(obj)
# print(obj_call)
