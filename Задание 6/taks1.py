def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int and float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)


assert average_num([1]) == 1
assert average_num([0, 1, 5, 100]) == 26.5
assert average_num([-50, 0, 50]) == 0
assert average_num(["1"]) == 1
assert average_num(["0", "1", "5", 100]) == 26.5
assert average_num(["-50", "0", "50"]) == 0
assert average_num(["A", 1]) == "Bad request"
assert average_num(["A", "1"]) == "Bad request"
assert average_num([0.5, 1.6, 5.4]) == 2.5
assert average_num([0.5, 1]) == 0.75
