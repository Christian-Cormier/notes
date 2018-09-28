#list uses []
#index starts at 0
#a = [[90,70,65], [0,100,5], [100,98,72]]
#a[1][2] = 5
# python ok with pressing enter after commas in a list

a = [[1,2,3],
     [4,5,6]]
##one way to traverse a 2d list

#def print_2dlist(lst):
#    for row in lst:
#        for element in row:
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()

#another way to traverse a 2d list
#for row in a:
#    for element in row:
#        print(element,end= ' ')
#    print()

#add all elements in 2d list
#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]
#print(sum)
#sum = 0
#for row in a:
#    for element in row:
#        sum += element
#print(sum)

#changing elements in 2d list
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        a[i][j] += 1
#        
#print_2dlist(a)


#Creating a 2d list
#x = [[0] * 5] * 8  Does Not Work!!!!
#x[0][0] = 100
#print(x)

#To make an m x n list
#m = 5
#n = 8
#x = [[0] * n for i in range(m)]
#x[0][0] = 100
#print(x)
        
        