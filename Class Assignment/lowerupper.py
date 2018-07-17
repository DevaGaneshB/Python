
def upplow(a):
    up=0
    lw=0
    for i in range(len(a)):
        if a[i].isupper():
            up=up+1
        if a[i].islower():
            lw=lw+1
    print("No. of uppercase ="+str(up))
    print("No. of lowercase ="+str(lw))
a=raw_input("Enter a string")
upplow(a)
