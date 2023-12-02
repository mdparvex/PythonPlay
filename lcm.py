
def compute_lcm(x,y):
    if x>y:
        grater = x
    else:
        grater = y
    
    while(True):
        if grater%x==0 and grater%y==0:
            lcm=grater
            break
        grater = grater+1

    return lcm

if __name__=='__main__':
    print(compute_lcm(7,10))