def giai_thừa(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    s=str(gt)
    s1=''
    for j in s:
        s1=s+j+','
   

n=int(input('nhập n='))
print(giai_thừa(n))
