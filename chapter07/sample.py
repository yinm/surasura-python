def add_10(num):
    if not isinstance(num, int):
        print('Invalid num')
        return False
    add_num = num + 10
    print('add_num is {}'.format(add_num))
    return add_num

print(add_10(10))
print(add_10('二十'))