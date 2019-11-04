from ..binary_search_tree import binary_search2


# def test_not_exists():
#      my_item = 5
#      my_arr = [1,2,3]
#      assert binary_search2(item = my_item, arr=my_arr,L = 0,R  =2) == -1
#
# def test_not_empty_arr():
#      my_item = 5
#      my_arr = []
#      assert binary_search2(item = my_item, arr=my_arr,L = 0,R  =2) == -1

def test_not_negative_index():
    my_item = 2
    my_arr = [-3,-2,0,2,3]
    res = binary_search2(item=my_item, arr=my_arr,L = 0,R  =2)
    assert res == 3