def find_max_tuple(data):
    best_tuple = None

    def traverse(item):
        nonlocal best_tuple

        if isinstance(item, tuple) and len(item) == 2:
            if best_tuple is None or best_tuple[1] < item[1]:
                best_tuple = item
        elif isinstance(item, list):
            for sub_item in item:
                traverse(sub_item)

    traverse(data)
    return best_tuple


test_1 = [("a", 10), [("b", 25), ("c", 5)], [("d", 15), [("e", 99), ("f", 40)]]]
print("Test 1 Result:", find_max_tuple(test_1))  # ('e', 99)

test_2 = [[("loss_1", -50), ("loss_2", -10)], [[("loss_3", -5)]]]
print("Test 2 Result:", find_max_tuple(test_2))  # ('loss_3', -5)

test_3 = [[], [[]]]
print("Test 3 Result:", find_max_tuple(test_3))  # None
