from __future__ import division
from collections import Counter
from collections import OrderedDict
from itertools import chain, combinations

def main():
    a = int(input("Enter the minimum support value in percentage please dont give % sign"))
    minsup=float(a/100)
    b=int(input("Enter the minimum confidence value in percentage please dont give % sign"))
    conf=float(b/100)
    #minsup=minsup*0.01
    '''
    Input path for Dataset
    '''
    path_to_dat="F:\\BigData\\Assignment1"
    data=[]
    d3={}
    d = {}
    ans=[]
    d2={}
    ans5=[]
    lis=[]
    lis1=[]
    i=0
    arr=[]
    arr1=[]
    dkeys=[]
    dkeys1=[]

    f = open("Dataset1.dat", "r")
    lines = f.readlines()
    for line in lines:

        a=line.strip().split()

        data.append(a)
    #print("data is",data)
    for dat in data:
        for element in set(dat):
            d[element]=d.get(element,0)+1
    #print ("d is",d)
    for i in d:
        dkeys.append(i)
    for i in d:
        dkeys1.append(d[i])
    #print("main First", arr)
    for element in d:
        x=support(minsup,element,d[element])
        if(x!=0):
            ans.append(int(x))

    for element in ans:
        lis.append([element])
    a=len(lis)
    #print("lis is ",lis)
    lis1.append(lis)
    d3keys=[]
    while (a != 0):

        d3 = perform(lis, data, minsup)
        for i in d3:
            d3keys.append(i)
        #print(d3keys)
        for i in d3:
            arr1.append(d3[i])
        #print(arr1)

        #print("main second",arr1)
        ans5=connection(d3,minsup)
        a=len(ans5)
        lis=ans5
        lis1.append(lis)
        #print(lis)
    if(a==0):
        print ("frequent",lis1[0:(len(lis1)-1)])
        closedItemset(lis1)
        maximalFrequent(lis1)
        #print(d3)
        associationrules(lis1,d3keys,arr1,dkeys,dkeys1,conf,minsup,d)

def maximalFrequent(lis1):
    closed = []
    closed1 = []
    test = []
    test1 = []
    test2 = []
    ans = []
    for element in lis1:
        for item in element:
            if (len(item) == 1):
                closed.append(item)
            else:
                closed1.append(item)

    for element in closed:
        for item in element:
            test1.append(item)

    test = generateSubset(closed1)
    for element in test:
        for item in element:
            test2.append(item)

    # print("test",test)
    for element in test:
        count = 0
        for item in test:
            if (set(element).intersection(set(item)) == set(element)):
                count = count + 1
        # print("element and count",element,count)
        if (count == 1):
            ans.append(element)
    # print("ans",ans)
    print("Maximal Frequent is  : ", list(set(test1) - set(test2)), ans)
    #print("Maximal Frequent is  ", list(set(test1) - set(test2)), closed1)

def closedItemset(lis1):
    closed=[]
    closed1=[]
    test=[]
    test1=[]
    test2=[]
    ans=[]
    for element in lis1:
        for item in element:
            if(len(item)==1):
                closed.append(item)
            else:
                closed1.append(item)



    for element in closed:
        for item in element:
            test1.append(item)

    test=generateSubset(closed1)
    for element in test:
        for item in element:
            test2.append(item)


    #print("test2",set(test2))
    for element in test:
        count=0
        for item in test:
            if(set(element).intersection(set(item))==set(element)):
                count=count+1
        #print("element and count",element,count)
        if(count==1):
            ans.append(element)
    #print("ans",ans)
    print("closed if 0.8 is taken : ",list(set(test1)-set(test2)),ans)
    print("closed if exact values are taken : ",closed,closed1)

def generateSubset(lis):
    l = []
    sub = []
    ans = []
    for item in lis:
        l.append(list(powerset(set(item))))
    # print("subsets are : ",l)
    for element in l:
        for item in element:
            if (item != ()):
                sub.append((item))
    # print("all elements are",sub)
    # print("all elements are set rep",(set(sub)))
    for element in set(sub):
        ans.append(list(element))
    #print("Final", ans)
    return (ans)

def powerset(iterable):

    xs = list(iterable)

    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

def associationrules(lis1,d3keys,arr1,dkeys,dkeys1,conf,sup,d):
    closed = []
    closed1 = []
    test = []
    test1 = []
    test2 = []
    ans = []
    out=[]
    #print("d3keys",d3keys)
    #print("arr1",arr1)
    for element in lis1:
        for item in element:
            if (len(item) == 1):
                closed.append(item)
            else:
                closed1.append(item)

    for element in closed:

            test1.append(set(element))
    #print("closed1",(closed1))
    test = generateSubset(closed1)
    #print("All subsets are",test)
    for element in test:
        out.append(set(element))
    #print(out)
   # print("arr1 is",arr1)
    count(test1,out,d3keys,arr1,dkeys,dkeys1,test,conf,sup,closed1,d)
    #print(out)
    #print("Association rules are still in progress")


def count(test1,out,d3keys,arr1,dkeys,dkeys1,lis1,conf,sup,closed1,d):
    arr=[]
    i=0
    arr2=[]
    j=0
    k=0
    #print("In count",out)
   # print(dkeys1)
    #print(closed1)

    #print("dkeys1",dkeys1)

    for j in closed1:
        i=0
        subs=generateSubset(list([j]))
        #print(subs)

        for k in arr1:
            for two in subs:
                if(len(two)==2):
                    twice=two
            if(j==k):
                for ele in subs:
                    ite = 0
                    if (len(ele) == 1):
                        #print (ele)
                        for each in dkeys:

                            if([int(each)]==ele):
                                #print (dkeys1[ite],ele)
                                a=d3keys[i]/dkeys1[ite]
                                #print(a)
                                if(a>conf):
                                    print(set(twice),"-",set(ele),"=>",set(twice).difference(set(ele)))
                                    lift=float(a/sup)
                                    print ("lift :",lift)
                                    if (lift < 1):
                                        print("Not Interesting rule")
                                    cosine=float(d3keys[i]/100000)/((sup*sup)*0.5)
                                    print ("cosine :",cosine)
                            else :
                                ite=ite+1

                #print(d3keys[i])

            else:
                i=i+1
    '''for element in test1:
        #print("element",element)
        j=j+1
        for item in dkeys:
           # print("item",set(item))
            if((element)==(set(item))):
                arr2.append([dkeys1[j],element])
    for element in out:
        i=i+1
        for item in arr1:
                if ((element)==(set(item))):
                    arr.append([d3keys[i],element])
    #print (arr)
    #print (lis1)'''
    '''for element in lis1:
        if(len(element)>1):
            a=(sup+0.05)/(sup)

            if(a>=conf):
                k=k+1
                for j in element:
                    print(element ,"-",element[1:len(element)],"=>",j,"confidence is",a)
                    if(k%2==0):
                        lift=float((a-0.04)/(sup+0.01))
                        print("lift :",lift)
                    else:
                        lift =float( (a - 0.06) / (sup+0.01))
                        print("lift :",lift)
                    if(lift<1):
                        print("Not Interesting rule")
                    if(k%2==0):
                        cosine=float((a)/((sup)**(0.5)))
                        print("cosine :",cosine)
                    else:
                        cosine =float( (a - 0.02) / ((sup)**(0.5)))
                        print("cosine :",cosine)'''



def connection(d2,minsup):
    ans=[]
    for element in d2:
        x=support(minsup,d2[element],element)
        if(x!=0):
            ans.append(x)
    #print(ans)
    return (ans)

def perform(ans1,data,minsup):
    ans2=[]
    ans3={}
    if (len(ans1) > 0):
        ans2 = club(ans1)
        ans3=calculate(ans2, data, minsup)
        return ans3

def club(ans):
    arr = []
    for i in range(len(ans)):
        data1=ans[i+1:(len(ans))]
        for j in data1:
            arr.append(ans[i]+j)

    #print("after club",arr)
    return arr

def calculate(arr,data,minsup):
    d={}

    for element in arr:
        #print(element)
        count=0
        set2=set(element)
        #print("set2",set2)
        for dat in data:
            arr1 = []
            for item in dat:
                arr1.append(int(item))

            set1=set(arr1)
            #print("set1",set1)
            if(set2.intersection(set1)==set2):
                    count=count+1
        d[count] = list(set2)
    #print("In calculate d={}",d)
    return (d)

def support(minsup,b,a):

    total=100000
    calsup=a/total

    if (calsup>minsup):

        return b

    else:
        return 0















if __name__=="__main__" :
    main()