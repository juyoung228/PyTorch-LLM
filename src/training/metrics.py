import math
from sklearn.metrics import mean_squared_error
import numpy as np


def MCRMSE(y_trues, y_preds):
    scores = []
    idxes = y_trues.shape[1]
    for i in range(idxes):
        #
        #
        # # RMSE
        scores.append(score)
    mcrmse_score = #
    return mcrmse_score, scores


def get_score(y_trues, y_preds):
    mcrmse_score, scores = #
    return mcrmse_score, scores


class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        #
        #
        #
        #


def asMinutes(s):
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


def timeSince(since, percent):
    now = time.time()
    s = now - since
    es = s / (percent)
    rs = es - s
    return '%s (remain %s)' % (asMinutes(s), asMinutes(rs))
