
class SinglyLinkedListNoDummy :     # ทำงานเหมือนกับ List (อ้าง อินเด็กซ์แบบเดียวกัน)
    class Node :                    # โหนดเก็บข้อมูล
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.tail = None
            self.size = 0
            
    def __str__(self):                # แสดงข้อมูลทุกตัวใน linked list
        s = ''
        p = self.head
        while p != None :
            if p.next !=None :
                s += str(p.data) + " -> "
            else :
                s += str(p.data)
            p = p.next
        return s
          
    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size         
            
    def isEmpty(self) :               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0         # len(self) == 0
        
    def indexOf(self,data) :          # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :             # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):           # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head is None :
          p = self.Node(data)
          self.head = p
          #self.head = self.Node(data,None)
          self.tail = p
          self.size += 1
        else :                        # เพิ่ม ในกรณีที่ไม่ใช่ Node แรก
          self.addTail(data)
          #self.insertAfter(len(self)-1,data)   #len(self) = จำนวนสมาชิก - 1 คือ index
          #self.tail = self.nodeAt(len(self)-1)
    
    def insertAfter(self,i,data) :       #เพิ่ม ข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        q = self.nodeAt(i)
        p = self.Node(data)
        #self.tail = p if q == self.tail else self.tail
        ##if q == self.tail :
        ##  self.tail = p
        p.next = q.next
        q.next = p
        #q.next = self.Node(data,q.next)
        self.size += 1
    
    def addTail(self,data) :
        q = self.tail
        p = self.Node(data)
        q.next = p
        self.tail = p
        self.size += 1

    def removeTail(self) :
        if self.size > 0 :
          q = self.nodeAt(len(self)-2)
          self.tail = q
          q.next = None
          self.size -= 1

    def deleteAfter(self,i) :            #ลบ โหนดข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        if self.size > 0 :  # len(self)
          q = self.nodeAt(i)  
          #if i == len(self)-2 :
          #  self.tail = q
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                 #ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if self.size > 0 :
          if i == 0 :    #ลบตัวแรก
            self.head = self.head.next
            self.size -= 1
          elif i == len(self) - 1 :
            self.removeTail()
          else :
            self.deleteAfter(i-1)          #ลบตัวก่อนหน้า
        
    def removeData(self,data) :          #ลบข้อมูลใน linked list
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          #self.head = self.Node(data,None)
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1
    
maxDigit = 0
maxDigitNev =0
currentDigit = 0
digitcap = 0
maxVal =0
minVal = 0
radix = input("Enter Input : ").split(" ")
L = SinglyLinkedListNoDummy()
nL = SinglyLinkedListNoDummy()
for e in radix :
    currentDigit = int(e)
    if maxVal < currentDigit and currentDigit >=0:
        maxVal = currentDigit
        maxDigit = len(str(currentDigit))
    elif minVal > currentDigit and currentDigit < 0 :
        minVal = currentDigit
        maxDigitNev = len(str(currentDigit))-1
    if int(e) >= 0:
        L.append(str(e))
    else :
        nL.append(str(e)[1:])
if maxDigitNev >= maxDigit:
    digitcap = maxDigitNev
else :
    digitcap = maxDigit
beforeRadix = " -> ".join(radix)
################ Positive #################
digit = -1
indx=0
digitList = [SinglyLinkedListNoDummy() for e in range(maxDigit+1)]
while indx < maxDigit+1 :
    if indx != 0:
        for i in range(10) :
            headDigit = digitList[indx-1].head
            while headDigit != None:
                if len(str(headDigit.data)) < -digit and i == 0:
                        digitList[indx].append(headDigit.data)
                elif len(str(headDigit.data)) >= -digit:
                    if i == int(str(headDigit.data)[digit]):
                        digitList[indx].append(headDigit.data)
                headDigit = headDigit.next
    else :
        for i in range(10) :
            headDigit = L.head
            while headDigit != None:
                if i == int(str(headDigit.data)[digit]) :
                    digitList[indx].append(headDigit.data)
                headDigit = headDigit.next
    indx+=1
    digit-=1
################ Positive #################

################ Negative #################
digit = -1
indx=0
digitListNev = [SinglyLinkedListNoDummy() for e in range(maxDigitNev+1)]
while indx < maxDigitNev+1 :
    if indx != 0:
        for i in reversed(range(10)) :
            headDigit = digitListNev[indx-1].head
            while headDigit != None:
                if len(str(headDigit.data)) < -digit and i == 0:
                        digitListNev[indx].append(headDigit.data)
                elif len(str(headDigit.data)) >= -digit:
                    if i == int(str(headDigit.data)[digit]):
                        digitListNev[indx].append(headDigit.data)
                headDigit = headDigit.next
    else :
        for i in reversed(range(10)) :
            headDigit = nL.head
            while headDigit != None:
                if i == int(str(headDigit.data)[digit]) :
                    digitListNev[indx].append(headDigit.data)
                headDigit = headDigit.next
    indx+=1
    digit-=1
################ Negative #################

radix_sort = SinglyLinkedListNoDummy()
radix_sort_display = SinglyLinkedListNoDummy()
posNum = digitList[-1].head
nevNum = digitListNev[-1].head
while posNum != None: 
    if nevNum == None:
        radix_sort.append(posNum.data)
        radix_sort_display.append(int(posNum.data))
        posNum = posNum.next
    else:
        radix_sort.append(nevNum.data)
        radix_sort_display.append(int("-"+str(nevNum.data)))
        nevNum = nevNum.next

check = 0
count = 1
stop = False
exp = 1
print("------------------------------------------------------------")
while not stop :
    print("Round : "+str(count))
    for i in range(10):
        display = radix_sort_display.head
        print(str(i)+" :",end=" ")
        while display != None:
            if  i == ((-display.data//exp)%10) and display.data < 0:
                print(display.data,end=" ")
                if i==0:
                    check+=1
            elif i == ((display.data//exp)%10) and display.data >= 0:
                print(display.data,end=" ")
                if i==0:
                    check+=1
            display = display.next
        print("")
    count +=1
    if check == radix_sort_display.size :
        stop = True
    check=0
    if len(str(exp)) > digitcap :
        stop = True
    exp *= 10
    print("------------------------------------------------------------")

print(str(count-2)+" Time(s)")
print("Before Radix Sort : ",end="")
print(beforeRadix)
print("After  Radix Sort : ",end="")
print(radix_sort_display)
