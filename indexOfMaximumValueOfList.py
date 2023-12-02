
def maxValue(value_list):
    larger_value=0
    for i in range(len(value_list)):
        if value_list[i]>larger_value:
            larger_value=value_list[i]
            idx=i

    return idx

if __name__=='__main__':
    print(maxValue([2,5,3,1,7,5,0,6,55]))
