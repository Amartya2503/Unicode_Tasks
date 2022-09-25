# u_rg=int(input("enter the upper range"))
# l_rg=int(input("enter the lower range"))

# j=bin(10)
# print(type(j))

# for i in range(u_rg, l_rg+1):
#     print(binary(i))
#creating dictionary :) :
# from re import A


def my_task(u_rg, l_rg) :
    res={ }
    binary={ }
    flag=0
    for i in range(u_rg, l_rg+1):
        # j=bin(i)
        binary[i] = bin(i)   
        m=int(bin(i)[2:])
        for k in range(0,m):
            
        
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
    
    
    return [res, binary]

