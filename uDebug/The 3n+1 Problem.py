def main():
    a, b = map(int, input().split())
    list = []
    list.append(b)
    c = b%2
    if c == 0:        
        t = int(b/2)
        list.append(t)
            
    else:
        t = 3*b+1
        list.append(t)
        
    print(list)
    length = len((list))
    print(length)
    
    
    #print(a,x,d)
main()