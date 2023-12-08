def exercise3():
    boolVerify: bool = False

    while boolVerify is False:
        number_str = input('Select the operation:'
                           '\n1- Sum'
                           '\n2- Less'
                           '\n3- Multiplication'
                           '\n4- Divide\n')
        number = int(number_str)
        num1 = int(input('Write number: '))
        num2 = int(input('Write number: '))

        if number == 1:
            result = num1 + num2
        elif number == 2:
            result = num1 - num2
        elif number == 3:
            result = num1 * num2
        else:
            result = num1 / num2

        print(result)

        verify = input('Do you want to continue? Type "s" to continue and "n" to stop: ')
        if verify == 's':
            boolVerify = False
        elif verify == 'n':
            boolVerify = True









