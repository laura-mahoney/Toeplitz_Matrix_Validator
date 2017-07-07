""" 
Give a matrix, determine if the diagonals are the same value, i.e. a valid topelitz matrix


    >>> is_toeplitz([[1,2,3,4,5,6],[6,1,2,3,4,5],[5,6,1,2,3,4],[4,5,6,1,2,3],[3,4,5,6,1,2],[2,3,4,5,6,1]])
    True



    >>> is_toeplitz([[1,2,6,4,5,6], [6,1,4,5,8,9], [5,6,1,2,3,4], [8,5,9,1,2,3], [3,3,5,6,4,7], [2,10,4,5,7,1]])
    False

"""

def is_toeplitz(input_matrix):

    #original length of the matrix, used to calculate j, the inner array
    original_length = len(input_matrix)-1

    #function gets called last, checks the top, right side of the matrix, slicing
    #each row off the bottom of the matrix after each diagonal above the middle diagonal
    #gets checked

    def top_toeplitz(input_matrix):
        #slice bottom off matrix after each recursive call
        input_matrix = input_matrix[:-1:]
        # print len(input_matrix)
        j = original_length #j is given a value corresponding to length of 5,max index
        i = len(input_matrix)-1 #i is given a value corresponding to length of 4, 3, 2, 1, 0

        #if matrix length goes below 2 after being sliced, return True because that
        #last diagonal has already been checked, and there are no more diagonal rows
        #to compare 
        if len(input_matrix) < 2:
            return True
        #if the matrix is greater than length of two, proceed to while loop
        else: 
            #while loop works from the bottom of the matrix up, i and j are decremented 
            while i >= 1 and j>1:
                #if the value equals the next diagonal value decrement i and j to check 
                #the next value 
                if input_matrix[i][j] == input_matrix[i-1][j-1]:
                    # print input_matrix[i][j]
                    i-=1
                    j-=1
                else:
                    #if diagonal values are not equal, return False
                    return False
                # print input_matrix[i][j]
            #call this function recursively 
            return top_toeplitz(input_matrix)


    #the bottom half and main diagonal of the matrix are checked first 
    def bottom_toeplitz(input_matrix): #start here
        #if the length of the matrix is less than 2, return True because all diagonals
        #have been checked
        if len(input_matrix) < 2:
            return True
        #initialize i and j at zero since we are starting from the uppermost left corner
        i = 0
        j = 0

        #while i and j are less than the length of the matrix, i.e. their values as indices
        #will never go over 5
        while i < len(input_matrix) and j<len(input_matrix):
            #if the adjacent diagonal is equal to the next diagonal, increment i and j to 
            #check the rest of diagonal
            if input_matrix[i][j] == input_matrix[-(i+1)][(len(input_matrix)-1-j)]:
                # print input_matrix[i][j]
                i+=1
                j+=1
            else:
                #if the diagonal is not equal return false 
                return False

        #recursively call the function on everything except for the first row of the
        #matrix since we check its diagonal first
        return bottom_toeplitz(input_matrix[1::])

    #both functions are called on the toeplitz here
    #if both functions return true, the top and bottom of matrix are toeplitz, 
    #this function returns True, else returns False 
    if bottom_toeplitz(input_matrix) and top_toeplitz(input_matrix): 
        return True

    else:
        return False
     


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED ***\n"


