import sys
def main():  
    a,b = map(int, input().split()) 
    list = [b] 
    while b != a:
        if b%2 == 0:
            b = b//2
            list.append(b)                
        else:
            b = (3*b) + 1
            list.append(b)
    print(len(list))
main()