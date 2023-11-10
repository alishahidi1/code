arr1 = [1,2,3,4,4]

def find_duplicate(arr):
    set_arr = set(arr)
    return len(set_arr) == len(arr)

print(find_duplicate(arr1))


