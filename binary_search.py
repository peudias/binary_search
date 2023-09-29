def binary_search(list, item):
    down = 0
    high = len(list) - 1

    while down <= high:
        mid = (down + high) // 2
        predict = list[mid]

        if predict == item:
            return mid;
        if predict > item:
            high = mid -1
        else:
            down =  mid + 1
    return None

my_list = [1,3,5,7,9]
print (binary_search(my_list, 3))  # expected returns 1
print (binary_search(my_list, -1)) # expected returns None