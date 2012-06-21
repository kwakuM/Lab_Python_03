n=50
count=0
for i in range(1,n+1):
    if n%i==0:
        pass
    else:
        print i
        count+=1
        if count ==10:
            break
print "count is",count
            
