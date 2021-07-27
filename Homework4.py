for i in range(1,100):
    result=1
    if i%3 == 0:
        sure="Fizz"
        result=2
    if i%5 == 0:
        sure="Buzz"
        result=2
    if i%3 == 0 and i%5 == 0:
        sure="Fizzbuzz"
        result=2
    if result ==1:
        p=1
        multiples=0
        while (p<100):
            if i%p == 0:
                multiples= multiples + 1
                p+= 1
            else:
                p=p+1
        if multiples ==2:
            sure="Prime"
            result=2

    if result != 1:
        print(sure)
    else:
        print(i)