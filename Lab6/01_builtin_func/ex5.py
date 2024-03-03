'''
Write a Python program with builtin function that returns True if all elements of the tuple are true.
'''
def all_true_tuple(tuple):
    return all(tuple)

tuple_1 = (True, True, False, True)
print(all_true_tuple(tuple_1))  
tuple_2 = (True, True, True, True)
print(all_true_tuple(tuple_2))  