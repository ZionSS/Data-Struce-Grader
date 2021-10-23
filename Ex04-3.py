import re
class Queue():
    def __init__(self):
        self.queue = []

    def aslist(self):
        return self.queue

    def enqueue(self, item):
            self.queue.append(item)

    def dequeue(self):
        if(self.isEmpty() != True):
            return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

    def peek(self):
        if(self.isEmpty() != True):
            return self.queue[0]
    def size(self):
        return len(self.queue)

q = Queue()
book,arg = input("Enter Input : ").split("/")
book_q = book.split(" ")
for i in book_q:
    q.enqueue(i)
arg_q = list(re.split(' |,',arg))
for i in range(len(arg_q)):
    if arg_q[i]=="E":
        q.enqueue(arg_q[i+1])
    elif arg_q[i]=="D":
        q.dequeue()

i = 0
temp=[]
dup_list=q.aslist()
while i < q.size():
    temp.append(dup_list.count(dup_list[i]))
    i +=1
temp2 = dict(zip(dup_list,temp))
mode_list={i for (i,j) in temp2.items() if j == max(temp) }
if len(mode_list)>1:
    print("NO Duplicate")
else:
    print("Duplicate")