data = [1,2,3,4,5,6,7,8,9]


def batch(iterable,n):
    l = len(iterable)
    for idx in range(0,l,n):        
        try:
            yield iterable[idx:min(idx+n,l)]
        except StopIteration:
            print("no more to yield")            
        
        
if __name__ == "__main__":
    x = batch(data,2)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
