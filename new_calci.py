print("----------------------------------------")
print(" Hello, Welcome to Kiran's Calculator")
print("----------------------------------------")
print('''This Calculator is an output of many 
     failures and Errors''' )
print("     Don't Dare to Copy")
print("----------------------------------------")
print('''In this calculator you perform addn, sub,
 multiplication, division of n numbers''')

print("----------------------------------------")
print('''So now Use Calculator made my kiran
         by Entering the numbers''')

#input and length and defining the other requisites

userin=str(input())
n=len(userin)
c=0
operands=[]
loc_ops=[]
mainans=0

#finding the no .of operators, operands and location of those...
for i in range(0,n):
    if (userin[i]=="+") or (userin[i]=="-" or (userin[i]=="*") or (userin[i]=="/") or (userin[i]=="%")):
        c=c+1
        operands.append(userin[i])
        # oploc=userin.index()   cant recognise the use currently
        loc_ops.append(i)
        # end of first loop
      
# print(userin)
# print(n)                      ##  trials
# print(operands)
# print(loc_ops)


# assigning the values to intergers for calculating purpose
if ( c == 1):
    for i in range(0,n):
        if (userin[i]=="+") or (userin[i]=="-" or (userin[i]=="*") or (userin[i]=="/") or (userin[i]=="%")):
            int1=int(userin[0:i])
            int2=int(userin[i+1:n+1])
            print(c)
            if userin[i] == "+":
                ans=int(int1+int2)
                # print(First+Second)
                
            elif userin[i] == "-":
                ans=int(int1-int2)
                # print(First-Second)
                
            elif userin[i] == "*":
                ans=int(int1*int2)
                # print(First*Second)
                
            elif userin[i] == "/":
                ans=int(int1/int2)
                # print(First/Second)
                
            elif userin[i] == "%":
                ans=int(int1%int2)
                # print(First%Second)
                
            else:
                print("Invalid Operation")
            mainans=ans
else:
            # new blocks are added above
            # indentation is changed below 
    for j in range(0,c):
        print(j)
        if j==0:
            int1=int(userin[0:(loc_ops[j])])
            int2=int(userin[(loc_ops[j]+1):(loc_ops[j+1])])
        elif j>0 and j!=c-1:
            int1=mainans
            int2=int(userin[(loc_ops[j]+1):(loc_ops[j+1])])
        else:
            int1=ans
            int2=int(userin[(loc_ops[j]+1):n])
        #end of initialization of variables
        print(int1,'\t',int2)
        if operands[j] == "+":
            ans=int(int1+int2)
            # print(First+Second)
            
        elif operands[j] == "-":
            ans=int(int1-int2)
            # print(First-Second)
            
        elif operands[j] == "*":
            ans=int(int1*int2)
            # print(First*Second)
            
        elif operands[j] == "/":
            ans=int(int1/int2)
            # print(First/Second)
            
        elif operands[j] == "%":
            ans=int(int1%int2)
            # print(First%Second)
            
        else:
            print("Invalid Operation")
        print(ans) #loop testing
        mainans=ans

print("----------------------------------------")
print("final ans for",userin,"is = ", mainans)
print("----------------------------------------")
print()
print("Thank You for using Kiran's Calculator")
print()
print("----------------------------------------")