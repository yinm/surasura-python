def add_10(num):
    try:
        add_num = num + 10
        print('add_num is {}'.format(add_num))
        return add_num
    except:
        print('Error!')

print(add_10(10))
print(add_10('二十'))
