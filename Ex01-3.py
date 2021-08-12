print("*** Election ***")
n=input("Enter a number of voter(s) : ")
x=list(map(int,input().split()))
vote_list=[]
temp=[]
duplicate_element = 0
if any(x)>=1 and any(x)<=20:
   x.sort()
   for elemnet in range(len(x)):
       if x[elemnet] >= 1 and x[elemnet] <= 20:
           vote_list.append(x[elemnet])
   if len(vote_list)== 0:
        print("*** No Candidate Wins ***")
   else:
        i = 0
        while i < len(vote_list):
            temp.append(vote_list.count(vote_list[i]))
            i +=1
        temp2 = dict(zip(vote_list,temp))
        mode_list={i for (i,j) in temp2.items() if j == max(temp) }
        if len(mode_list)>1:
            print("*** No Candidate Wins ***")
        else:
            print(list(mode_list)[0])
else:
    print("*** No Candidate Wins ***")