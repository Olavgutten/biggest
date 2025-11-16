#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 13:22:10 2025

@author: ofurn
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 13:00:51 2025

@author: ofurn
"""

import yfinance as yf
import matplotlib.pyplot as plt

aapl = yf.download("PLTR", start="2025-01-01", end="2025-11-16")

print(aapl)


plt.plot(aapl.index, aapl["Close"])
plt.plot(aapl.index, aapl["High"])
plt.plot(aapl.index, aapl["Low"])
plt.show()
plt.close()

returns = aapl["Close"].pct_change()

plt.plot(returns.index, returns)
plt.show()
plt.close()


plt.hist(returns, bins=40, edgecolor="black")
plt.show()



