#Definition
import random

def binary_search( data, objective):

    result = False
    start = 0 
    end = len(data) -1
    steps = 0

    for i in data:
        
        steps += 1

        if start > end:
            result = False
            break
            

        mid = (start + end) // 2
        
        if data[mid] == objective :
            result = mid
            break

        elif data[mid] > objective :
            end = mid - 1 
        
        else:
            start = mid + 1

    return {
        "objective":objective,
        "index": result,
        "steps": steps
    }
         



if __name__ == '__main__':
    
    data = range(0, 90000000000)
    
    result = binary_search( data, random.randint(0,90000000000) )
    
    # print(data)
    print(result)
    print(data[result['index']])