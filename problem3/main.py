def join_array_remove_duplicate(arrayA, arrayB):
    result_array = arrayA.copy() 
    for item in arrayB:
        if item not in result_array:
            result_array.append(item)
    
    unique_result_array = []
    for item in result_array:
        if item not in unique_result_array:
            unique_result_array.append(item)

    return unique_result_array

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
