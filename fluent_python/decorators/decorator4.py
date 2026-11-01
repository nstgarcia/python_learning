def make_averager_w():
    count = 0
    total = 0 

    def averager(new_value):
        #this is wrong because it's assigned and thus it becomes a local
        # count =0 is a number and is immutable
        count +=1
        total +=new_value
        return total/count
    return averager

def make_averager():
    count = 0
    total =0 

    def averager(new_value):
        nonlocal count, total
        count +=1
        total +=new_value
        return total/count
    return averager
