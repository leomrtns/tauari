try:
    import tauari_c
except:
    print ("Tauari:: could not load C library 'tauari_c', maybe it's not compiled yet")
import logging
logger = logging.getLogger(__name__)
logger.propagate = False
stream_log = logging.StreamHandler()
log_format = logging.Formatter(fmt='Tauari %(asctime)s [%(levelname)s] %(message)s', datefmt="%Y-%m-%d %H:%M")
stream_log.setFormatter(log_format)
stream_log.setLevel(logging.WARNING)
logger.addHandler(stream_log)

def tauaritest(s1 = None, s2 = None):
    print(tauari_c.testfunction(s1, s2))

def tauaritest2():
    print(tauari_c.test2())

def get_version ():
    import pkg_resources  # part of setuptools
    return pkg_resources.require("tauari")[0].version

if __name__ == '__main__':
    print (f"Tauari version ", get_version())
