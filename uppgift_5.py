def copy_list(old_list):
    return old_list.copy()

list = ["Messi", "Ronaldo", "Neymar"]

print(copy_list(list))

new_list = copy_list(list)

list[0] = "ett"

print(list)
print(new_list)
