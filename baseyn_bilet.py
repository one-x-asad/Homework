def x(github):
    if github >= 1 and github <= 5:
        print("sizga tekin")
    elif github >= 6 and github <= 15:
        print("kirish narxi 50000")
    elif github >= 16 and github <= 25:
        print("kirish narxi 70000")
    elif github >= 26 and github <= 40:
        print("kirish narxi 65000")
    elif github >= 41 and github <= 50:
        print("kirish narxi 50000")
    elif github >= 51 and github <= 70:
        print("ha otam nima bo'lyapti uyingizga borib damingizni oling")
    else:
        print("siz shu yerda vafor etsangiz biz jinoiy javobgarlikka tortilishimiz mukin shu sababli kira olmaysiz")

x(3)
x(12)
x(20)
x(35)
x(46)
x(65)
x(99)
