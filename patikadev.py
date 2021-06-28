m = [[1, 2], [3, 4], [5, 6, 7]]

print([i[::-1] for i in m[::-1]])

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(old_list):
    for element in old_list:
        if type(element) == list:
            flatten_list(element)
        else:
            new_list.append(element)
    return new_list

new_list = []
print(flatten_list(L))
