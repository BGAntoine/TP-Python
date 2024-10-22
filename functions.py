def several_zeros():
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return list

def several_zeros_custom(nb_zeros = 10):
    list2 = []
    for i in range(nb_zeros):
        list2.append(0) 
    return list2
    
def matrix(rows, cols):
    list3 = []
    for x in range(rows):
        list3Bis = []
        list3.append(list3Bis)
        for y in range(cols):
            list3Bis.append(0)
    return list3
            
class Matrix:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__matrix = matrix(self.__rows, self.__cols)

    def get_value(self, row, col):
        result = self.__matrix[row][col]
        return result
    
    def __eq__(self, other):
        result2 = self.__matrix == other.__matrix
        return result2

def my_sort(my_list: [int]) -> [int]:
    my_tableau = my_list
    for a in range(len(my_tableau)-1) :
        for b in range(len(my_tableau)-1-a):
            if my_tableau[b+1] < my_tableau[b] :
                my_tableau[b+1], my_tableau[b] = my_tableau[b], my_tableau[b+1]
    return my_tableau
    







if __name__ == '__main__':
    print(several_zeros())
    
    print(several_zeros_custom(5))
    print(several_zeros_custom())
    
    print(matrix(2,3))
    
    m1 = Matrix(2,3)
    m2 = Matrix(2,3)
    print(m1 == m2)
    
    
    x = [3,5,7,4,1,8]
    print(my_sort(x))