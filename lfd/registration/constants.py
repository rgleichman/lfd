import numpy as np

class TpsConstant(object):
    N_ITER        = 20
    EM_ITER       = 1
    REG           = (.1, .0001)
    RAD           = (.01, .0001)
    ROT_REG       = np.r_[1e-4, 1e-4, 1e-1]
    OUTLIER_PRIOR = .1
    OURLIER_FRAC  = 1e-2

class TpsGpuConstant(TpsConstant):
    MAX_CLD_SIZE       = 150
    BEND_COEF_DIGITS   = 6
    OUTLIER_CUTOFF  = 1e-2
