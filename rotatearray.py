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
        

def rotate2(nums, k):
    length = len(nums)
    pivot = k % length
    if length == 0 or pivot == 0:
        return
    part_1 = nums[:length-pivot]
    part_2 = nums[length-pivot:]
    len_1, len_2 = len(part_1), len(part_2)

    def switch_array(arr, a_start, a_end, b_start, b_end):
#        print a_start, a_end, b_start, b_end
        if a_start > a_end or b_start > b_end:
            print 'end of recursive'
            return
        len_a, len_b = a_end - a_start + 1, b_end - b_start + 1

        if len_a >= len_b:
            i = 0
            while i < len_b:
                arr[a_start+i], arr[b_start+i] = arr[b_start+i], arr[a_start+i]
                i += 1
            print 'len of first array is bigger than or equal to len of second array',
            print arr
            print arr[len_b], arr[a_end], arr[b_start], arr[b_end]
            if b_end != 6: return
            switch_array(arr, a_start+len_b, a_end, b_start, b_end)
        elif len_a < len_b:
            i = 0
            while i < len_a:
#                print i+b_end-len_a+1
                arr[a_start+i], arr[i+b_end-len_a+1] = arr[i+b_end-len_a+1], arr[a_start+i]
                i += 1
#            print 'len of first array is smaller than len of second array',
#            print arr
#            print a_start, a_end, b_start, b_end-len_a
#            print arr[a_start], arr[a_end], arr[b_start], arr[b_end-len_a]
            switch_array(arr, a_start, a_end, b_start, b_end-len_a)

    switch_array(nums, 0, length - pivot - 1, length - pivot, length-1)


test1 = [1,2,3,4,5,6,7]
rotate(test1, 3)
print test1

test1 = [1,2,3,4,5,6,7]
rotate(test1, 10)
print test1


test1 = [1,2,3,4,5,6,7]
rotate(test1, 9)
print test1
