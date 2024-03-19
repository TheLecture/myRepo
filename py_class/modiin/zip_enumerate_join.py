def my_func(char,list):
    good_strings = []
    if len(list)==0:
        return "Eror, empty list"
    for item in list:
        if len(item)>=3:
            good_strings.append(item)
    if len(good_strings)==0:
        return "Eror: no strings with sufficient length."
    else:
        return char.join(good_strings)
    
    
    
    
words_list = ["abcd","ef","ghi","jklmnop"]
words_list1 = []
words_list2 = ["ad","ef","hi","p"]

print(my_func("-",words_list))
print(my_func("_",words_list1))
print(my_func("$",words_list2))
    