def cat_dog(s):
    count_cat = s.count("cat")
    count_dog = s.count("dog")
    return count_cat == count_dog
print(cat_dog('catdog'))  
print(cat_dog('catcat'))  
print(cat_dog('1cat1cadodog'))  
