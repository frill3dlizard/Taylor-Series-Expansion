# Taylor-Series-Expansion
The code allows Taylor series to be expanded into the polynomial form. Example below:

Given a Taylor series for $\frac{1}{x}$ centered at 6:
```math
\sum_{n=0}^N \frac{(-1)^n (x-6)^n}{(6)^{n+1}}$$
```
To put this series into the polynomial form, i.e. $\alpha_0 +\alpha_1x+\alpha_2x^2+\dots$, we must at every 'n' (starting from 0) expand the $(x-6)^n$ bracket using the binomial formula, and multiply by the constants. Then store in an array these $\alpha_i$'s such that for each 'n' in the series, we can add them together to complete the sum. In mathematical writing, it would be as below:

We wish to compute:
```math
\sum_{n=0}^2 \frac{(-1)^n (x-6)^n}{(6)^{n+1}}$$
```
The function ```python array(2, 6, taylor)``` will iterate over ```python taylor(n,6)```, creating the array as follows:
```math
frac{(-1)^0 (x-6)^0}{(6)^{0+1}}$$ = [\alpha_0]
```
```math
\frac{(-1)^1 (x-6)^1}{(6)^{1+1}}$$ = [\beta_0, \beta_1]
```
```math
\frac{(-1)^2 (x-6)^2}{(6)^{2+1}}$$ = [\gamma_0, \gamma_1, \gamma_2]
```
Final array:
```math
[\alpha_0+\beta_0+\gamma_0, \beta_1+\gamma_1, \gamma_2]
```
