bid=list(map(int,input("Enter All Bid : ").split()))
bid.sort()
bidPay_index=len(bid)-2
maxBid = max(bid)
maxBid_duplicate = 0
if len(bid)>1:
    for element in range(len(bid)):
        if maxBid == bid[element]:
            maxBid_duplicate+=1
    bidPay=bid[bidPay_index]
    if maxBid_duplicate > 1:
        print("error : have more than one highest bid")
    elif maxBid_duplicate == 1:
        print("winner bid is",maxBid, "need to pay",bidPay)
else :
    print("not enough bidder")