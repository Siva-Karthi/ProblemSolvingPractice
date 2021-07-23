
#1,2,4,5,3

# def dfs(array, root):
#    tempArray = array[root]
#    print(root)
#     for(var i=0; i<tempArray.length;i++){
#         dfs(array, tempArray[i]);
#     }
#
def dfs(arry, root):
    tempArray = array[root]
    print(root)
    for child in tempArray:
        dfs(arry, child)

if __name__ == '__main__':
    array = {1:[2,3],2:[4,5],3:[],4:[],5:[]}
    dfs(array, 1)
