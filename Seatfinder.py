print("Train Seat Finder")
seat_num= [19,24,34,39,47,57,98]
n = len(seat_num)
target = 47
steps = 0
for i in range(n):
    steps += 1
    if seat_num[i] == target:
        print("Linear Search: index =", i, "Steps:", steps, "O(n)")
        break

lo, hi,steps = 0, n-1,0
while lo<=hi:
    mid = (lo+hi)//2
    steps += 1
    if seat_num[mid]==target:
        print("Binary Search:index","=",mid,"Steps:",steps,"0(logn)")
        break
    elif seat_num[mid]<target:
        lo = mid+1
    else:
        hi = mid-1
print()

def binary_search(seat_num,lo,hi,target,calls=0):
    calls+=1
    if lo>hi:
        return-1,calls
    mid = (lo+hi)//2
    if seat_num[mid]==target:
        return mid,calls
    elif seat_num[mid]<target:
        return binary_search(seat_num,mid+1,hi,target,calls)
    else:
        return binary_search(seat_num, lo, mid-1, target, calls)
result, calls = binary_search(seat_num,0,n-1,target)
print("Recursive Search:index",result,"|Calls=",calls,"0(logn)")
print()