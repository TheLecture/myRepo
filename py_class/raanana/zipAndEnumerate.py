

# (1,4) - item -- 0
# (2,5) - item -- 1
# (3,6) - item -- 2

def multy_func(list1,list2):
    multy_list=[]
    for item in zip(list1,list2):
        multy_list.append(item[0]*item[1])
    return multy_list



nums1=[1,2,3,99,103]
nums2=[4,5,6,3]
nums3=[7,8,9]
nums4=[10,11,12]
nums5=[1,2,3]
nums6=[4,5,6]
print(multy_func(nums1,nums2))
print(multy_func(nums3,nums4))