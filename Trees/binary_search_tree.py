# [-10,-1,0,1,2,3]

def binary_search(item, arr, L,R) -> int:
    """
    take item , get mid index and element of this index as root
    if item is the root element , well and good return current index
    else if item < root then search on elements which are only left to the root
    else if item > root then search on elements which are only right to the root
    else item not in array


    ---------------------------------

    since its recursion and next call will get get sub array only and mid index will vary and we can
    :param item:
    :param arr:
    :return:
    """
    if R>=L:
        mid = (L + R) / 2
        index = int(length / 2)
        root = arr[index]
        if item == root:
            print(item, root, index, arr, pre_index)
            print("got it")
            return abs(index + pre_index)
        elif item < root:
            print(item, root, index, arr, pre_index)
            print("go left")
            return pre_index - binary_search(item,arr[:index], index)
        elif item > root:
            print(item, root, index, arr, pre_index)
            print("go right")
            return pre_index + binary_search(item,arr[index+1:], index)

    print("item not available go out")
    return -1



def binary_search2(item, arr, L,R) -> int:
    """
    take item , get mid index and element of this index as root
    if item is the root element , well and good return current index
    else if item < root then search on elements which are only left to the root
    else if item > root then search on elements which are only right to the root
    else item not in array


    ---------------------------------
 res = binary_search2(item=my_item, arr=my_arr)
    since its recursion and next call will get get sub array only and mid index will vary and we can
    :param item:
    :param arr:
    :return:
    """
    if R>=L:
        mid = int(L + R) / 2
        index = int(mid)
        root = arr[index]
        if item == root:
            return index
        elif item < root:
            return  binary_search2(item,arr,L,index)
        elif item > root:
            return binary_search2(item,arr,index,R)
    return -1




arr = [1,3,5]
print(arr.index(5))