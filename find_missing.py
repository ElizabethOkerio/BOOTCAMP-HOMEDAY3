def find_missing(arr1, arr2):
    result=0
    if len(arr1)==len(arr2):
    	return result
    for num in arr1+arr2:
        result^=num
    return result