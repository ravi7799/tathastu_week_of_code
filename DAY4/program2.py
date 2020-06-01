test_list = [(2, 6, 1), (2, 7, 12), (1, 8, 0), (3, 9, 10)]
print("The original list is : " + str(test_list))
N = 0
test_list.sort(key = lambda x:x[N])

print("List after sorting tuple by Nth index sort : " + str(test_list))
