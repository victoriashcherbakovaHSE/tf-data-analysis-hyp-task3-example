import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 871302863

def solution(x: np.array) -> bool:
    alpha = 0.02
    mu=300
    n = len(x)
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)
    se = s / np.sqrt(n)
    t_stat = (x_bar - mu) / se
    t_crit = t.ppf(alpha, n-1)
    return t_stat < t_crit
