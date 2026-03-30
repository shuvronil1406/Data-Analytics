import numpy as np
# print(np.__version__)
# array = np.array([1,2,3,4])
# print(type(array))
# print(array*2)  
# array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                #   [['J','K','L'],['M','N','O'],['P',"q",'R']],
                #   [['s','t','u'],['v','w','x'],['y','z','_']]])
# print(array[0,0,2]+array[0,0,0]+array[2,0,1])
# print(array.ndim)
# print(array.shape)
# scores = np.array([91,55,100,73,92,80])
# print(scores>=90)


# broadcasting:-
# the dimension should either match or one of them should be 1 to be able to broadcast
# array2=np.array([[1,2],
                #  [2,3],
                #  [3,4],
                #  [4,5]])
# array1=np.array([[1,2,3,4],
                #  [4,5,6,7],
                #  [1,1,1,1],
                #  [1,1,1,1]])
# print(array1.shape)
# print(array2.shape)
# print(array1*array2)

# array2=np.array([[1],
                #  [2],
                #  [3],
                #  [4],
                #  [5],
                #  [6],
                #  [7],
                #  [8],
                #  [9],
                #  [10]])
# array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
# print(array1.shape)
# print(array2.shape)
# print(array2*array1)
#filtering

#boolean indexing
ages = np.array([[19,20,55,40,30,17,13,70,80,60,35,27,59],
                [2,4,3,5,6,8,78,86,82,91,97,126,264]])
# teenagers = ages[ages<=19]
adults = ages[(ages>18) & (ages<=60)]  #we have to use "&" instead of "and" as numpy is written in c, so it uses operators as there in c, "|" instead of "or".
evens=ages[ages%2==0]
# print(evens)

#where function:-
human = np.where(ages<=100,ages,-1)    # syntax -> (condition, original array, expression to be replaced with if condition doesn't satissfy)
# print(human)    #shape is same as original array

#random numbers
rng = np.random.default_rng(seed=1)  #created an objecct rng.,#seed=1 fixes one randomly generated number or array.
# print(rng.integers(1,7)) #7 is exclusive
# print(rng.integers(low=1,high=7)) #7 is exclusive
# print(rng.integers(low=1,high=7,size=3)) #1d
# print(rng.integers(low=1,high=7,size=(3,2))) #2d

# for floating points



