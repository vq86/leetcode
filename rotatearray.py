# Problem description:
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].


def rotate(num, k):
    length = len(num)
    step = k % length
    end = length - step - 1
    second = num[end+1:]
    while end >=0 :
        num[end+step] = num[end]
        end -= 1
    i = 0
    while i<len(second):
        num[i] = second[i]
        i += 1 
        


test1 = [1,2,3,4,5,6,7]
rotate(test1, 3)
print test1

test1 = [1,2,3,4,5,6,7]
rotate(test1, 10)
print test1


test1 = [1,2,3,4,5,6,7]
rotate(test1, 9)
print test1
