
# simple view of the ranges of the match lengths between reads and the query

import pandas as pd
import numps as np

df3 = pd.read_csv("./output/results.csv")

from matplotlib import pyplot as plt
#plot 1
(counts, bins) = np.histogram(df3.num_match_char.tolist()[:600], bins=range(100))
factor = 1
plt.hist(bins[:-1], bins, weights=factor*counts)
plt.show()


#plot 2 (taken the log to vule the significantly lower valure)
bins = 10**(np.arange(0,4))
print ("bins: ", bins)
plt.yscale('log')
plt.hist(df3,bins=10) 

plt.show()