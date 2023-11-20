def palindrome(name:str):
    ans=[]
    for i in range(len(name)):
        for j in range(i+1,len(name)):
            if name[i]==name[j]:
                a=i+1
                b=j-1
                while a<b:
                    if name[a]==name[b]:
                        a+=1
                        b-=1
                    else:
                        break
                if a>=b:
                    ans.append(name[i:j+1])
    return ans
                
name=input("Enter a string: ")
print(palindrome(name))
