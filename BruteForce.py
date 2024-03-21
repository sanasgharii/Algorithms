import typing
import numpy as np
import math

#########################################   SELECTION SORT   ######################################### 
def selection_sort(array: typing.List[float]) -> typing.List[float]:
    #iterate over all array elements
    for i in range(len(array)-1):
        #find the min in the remaining array
        #unsorted array
        min_idx  = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        #swab the found minimum element with the first element        
        array[i], array[min_idx] = array[min_idx], array[i]
        
    return array
          
# print(selection_sort([2,4,5,1,3]))

######################################  EVALUATE A POLYNOMIAL   #######################################
def evaluate_polynomial (a: typing.List[float],
                         x: float) -> float:
    evaluation = 0 
    for i in range(len(a)):
        power = 1 
        for j in range(i):
            power *= x
        evaluation += a[i] * power
    return evaluation

#following is more efficient
#complexity of Θ(n)
def evaluate_polynomial (a: typing.List[float],
                         x: float) -> float:
    evaluation = a[0] 
    power = 1
    
    for i in range(1, len(a)):
        power *= x
        evaluation += a[i] * power
    return evaluation

#######################################  PATTERN RECOGNITION   ########################################

def pattern_match(pattern: str, text: str)->int:
    m = len(pattern)
    n = len(text)
    
    for i in range(n-m+1):
        j = 0 #at the beginning of iteration j=0 
              #means we start the pattern from the beginning
        while j < m and pattern[j] == text[i + j]:
            j +=1
        if j == m:
            return i 
    return -1

# pattern = "ABABCABAB"
# text = "ABABDABACDABABCABAB"
# print(pattern_match(pattern, text))

##########################################  CLOSEST PAIR   ############################################
def closest_pair(points: typing.List[typing.Tuple[float, float]]) -> typing.Tuple[int, int]:
    closest_pair = None
    min_distance = np.inf
    print(min_distance)
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):  # Start j from i+1 to avoid comparing a point with itself
            distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            
            if distance < min_distance:
                min_distance = distance  # Correctly update min_distance
                print(min_distance)
                closest_pair = (i, j)
                
    return closest_pair

# points = [(0,0), (1,5), (2,1), (-1,4)]
# print(closest_pair(points))
