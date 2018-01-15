c = get_config()
c.InteractiveShellApp.exec_lines = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.max_colwidth', -1)

%matplotlib inline
""".split('\n')
# c.InteractiveShellApp.matplotlib = 'inline'