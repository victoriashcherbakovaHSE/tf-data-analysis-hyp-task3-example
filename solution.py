import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 871302863

def solution(x: np.array) -> bool:
    alpha = 0.02
    t_statistic, p_value = ttest_1samp(x, 300)
    if p_value/2 < alpha and t_statistic > 0:
        return True
    else:
        return False
