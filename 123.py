def HN(n,N,T,D):
    if (n==1):
        print("D:",n,"move",N,"=>",D)
        return()
    HN(n-1,N,D,T)
    print("D:",n,"move",N,"=>",D)
    HN(n-1,N,T,D)
HN(3,"N","T","D")