# studies citation lag frequencies: seems to be a powerlaw, stabilizes to an exponent
# of ~60 after a few decades.

__author__ = 'mik'

import re
import glob
from collections import defaultdict
import numpy as np
import scipy as sp

SOUre = re.compile("SOU\s*(\d+)\s*:\s*(\d+)")

references = defaultdict(set)

for filename in glob.glob("TXT/*/*txt"):
    match = SOUre.search(filename)
    ref = match.groups()
    print("%s:%s" % ref)
    with open(filename, 'r') as f:
        soutext = f.read()
        for match in SOUre.finditer(soutext):
            print("\t%s:%s" % match.groups())
            references[ref].add(match.groups())

difftimes = dict()
for k in references:
    year = int(k[0])
    difftimes[k] = list()
    for y,s in references[k]:
        difftimes[k].append(year-int(y))


## exponential distribution(s)?
freqs = np.histogram([dt for k in difftimes for dt in difftimes[k]],
    bins=range(60), density=False)[0]
decadefreqs = np.array([np.histogram([dt for k in difftimes for dt in difftimes[k] if k[0][2]==dec],
    bins=range(60), density=False)[0] for dec in ['2','3','4','5','6','7','8','9']])
logfreqs = np.log(freqs)
decadelogfreqs = np.log(decadefreqs)
decadelogfreqs[np.isinf(decadelogfreqs)] = np.nan



for i,dec in enumerate([1920,1930,1940,1950,1960,1970,1980,1990]):
    try:
        model = sm.OLS(arange(59), sm.add_constant(decadelogfreqs[i,:]), missing='drop')
    except ValueError:
        continue
    results = model.fit()
    print(dec)
    print(results.summary())
