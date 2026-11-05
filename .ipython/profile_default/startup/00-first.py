#
# builtins
#
from importlib import reload
from datetime import datetime as dt, timedelta, time as dt_time
import time
import json
import pickle


#
# IPython
#
try:
    from IPython import get_ipython

    ipy = get_ipython()
    ipy.run_line_magic("load_ext", "autoreload")
    ipy.run_line_magic("autoreload", "2")
    ipy.run_line_magic("matplotlib")
    del ipy
except:
    print("Can't import IPython")

#
# Numpy/Pandas
#
try:
    import numpy as np
    import pandas as pd

    pd.options.display.max_rows = 200
    pd.options.display.max_colwidth = 200
except:
    print("Can't import pandas")


#
# Matplotlib
#
try:
    import matplotlib.pyplot as plt

    plt.ion()
except:
    print("Can't import matplotlib")
