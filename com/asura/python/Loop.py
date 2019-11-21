for i in range(1, 10):
    for k in range(1, i + 1):
        a = ""
        if i * k < 10:
            a = "     "
        else:
            a = "    "
        print("%d * %d = %d" % (i, k, i * k), end=a)
    print("")
