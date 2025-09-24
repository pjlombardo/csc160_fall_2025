def get_max(v1,v2,v3):
    if v1 < v2:
        m1 = v2
    else:
        m1 = v1
    
    if m1 < v3:
        return v3
    else:
        return m1
    
def get_max2(v1, v2, v3):
    if v1 < v2:
        if v2 < v3:
            return v3
        else:
            return v2
    else:
        if v1 < v3:
            return v3
        else:
            return v1

print(get_max2(1, 2, 3))
print(get_max2(3,2,1))
print(get_max2(2,1,3))
