u_rg=int(input("enter the upper range"))
l_rg=int(input("enter the lower range"))
res={ }
flag=0

# j=bin(10)
# print(type(j))

# for i in range(u_rg, l_rg+1):
#     print(binary(i))
#creating dictionary :) :

for i in range(u_rg, l_rg+1):
    j=bin(i)
    m=int(j[2:])
    for k in range(0,len(j)):
            
        
        if (m%2 != 0):
            flag += 1
        else:
            flag = 0

        if flag >= 2:
            res[i]=True
            break
        else:
            res[i]= False
        m=int(m/10)
    
print(res)