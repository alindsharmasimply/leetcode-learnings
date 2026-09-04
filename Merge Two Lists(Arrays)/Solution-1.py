l1 = [1, 4, 6, 8]
l2 = [2, 4, 7, 9, 10]


def merge_lists():
    l3 = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    # This syntax is important.
    # Here we are appending the remaining portion of the list
    # The catch is that only either one of the lists will have any items remaining in it.
    return l3 + l1[i:] + l2[j:]


print(merge_lists())
