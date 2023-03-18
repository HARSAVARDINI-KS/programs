n=int(input("enterrr"))
i=2
factor=[]
while i*i <=n:
    if n%i:
        i+=1
    else:
        n//=i
        factor.append(i)
if n>1:
    factor.append(n)
factor=set(factor)
factor=list(factor)
initmul=1
for digits in factor:
    initmul=initmul*digits
print(initmul)
