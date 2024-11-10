txt = 'This dog runs faster than the other dog dude!'

#print(txt.split())

def find_dog(txt):
    lst = txt.split()
    cnt = 0
    for txt in lst:
        if txt.find('dog') > -1:
            cnt +=1
    print(cnt)


find_dog(txt)