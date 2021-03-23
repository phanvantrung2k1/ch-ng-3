def get_sum(*num):# nhập đầu vào với số lượng tùy ý
    tmp=0
    for i in num:
        tmp+=i
    return(tmp)
result=get_sum(1,2,3,4,5)
print(result)
