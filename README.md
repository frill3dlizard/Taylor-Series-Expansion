# Taylor-Series-Expansion
The code allows Taylor series to be expanded into the polynomial form. Example below:

Given a Taylor series for $\frac{1}{x}$ centered at 6:
```math
\sum_{n=0}^N \frac{(-1)^n (x-6)^n}{(4)^{n+1}}$$
```
To put this series into the polynomial form, i.e. $\alpha_0 +\alpha_1x+\alpha_2x^2+\dots$, we must at every 'n' (starting from 0) expand the $(x-6)^n$ bracket using the binomial formula, and multiply by the constants. Then store in an array these $\alpha_i$'s such that for each 'n' in the series, we can add them together to complete the sum. In mathematical writing, it would be as below:

