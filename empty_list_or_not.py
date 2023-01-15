def check_list(input_list):
    if input_list == []:
        result = print('The input list is EMPTY.')
    else:
        result = print(f'The input list is NOT EMPTY and contains {input_list} elements.')
    return result

if __name__ == '__main__':
    
    print(f"Test 1:{check_list([2,1])}")
    
    print(f"Test 2:{check_list([])}")
