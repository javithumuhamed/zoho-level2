def calc(les):
    #mid value
    mid=int(len(les)/2)
    arr=[]  
    #creating printable values
    reach=''
    #creating array with proper printables
    for i in range(0,len(les)):
        if(mid<len(les)):
            reach=reach+les[mid]
            arr.append(reach)
            mid+=1
        else:
            mid=0
            reach=reach+les[mid]
            arr.append(reach)
            mid+=1
    n=len(les)
    #printing with proper indentations
    for i in arr:
        for j in range(0,n-len(i)):
            print("",end=" ")
        print(i)


if __name__=='__main__':
    input1=input()
    calc(input1)
