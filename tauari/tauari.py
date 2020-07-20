try:
    import tauari_c
except:
    print ("Tauari:: could not load C library 'tauari_c', maybe it's not compiled yet")

def tauaritest(s1 = None, s2 = None):
    print(tauari_c.testfunction(s1, s2))

def tauaritest2():
    print(tauari_c.test2())
