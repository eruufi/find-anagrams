def is_anagram(s1,s2):
    print(len(s1),len(s2))
    l1 = len(s1)
    l2 = len(s2)
    count = 0
    if l1 == l2:
        for i in s1:
            for j in s2:
                if 1 == j:
                    count += 1
                    s1.replace(1,'',1)
                    s2.replace(j,'',1)
                    break
    if count == l1:
        return True
    return False

print(is_anagram("pot","top"))