# Taylor-Series
A Taylor series is an approximation for an infinitely differentiable function about a point $x=a$ by summing over the the following formula:
```math
\sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n = f^{(0)}(a)+\frac{f^{(1)}(a)}{1!}(x-a)+\frac{f^{(2)}(a)}{2!}(x-a)^2+\dots$$
```
Although the sumation form is useful in most applicaitons, some may require the fully extended polynomial form. This is what the code aims to acheive for a few common functions, such as $\frac{1}{x}, sin(x), cos(x), ln(x)$.

# Taylor-Series-Expansion
The code allows Taylor series to be expanded into the polynomial form. Example below:

Given a Taylor series for $\frac{1}{x}$ centered at 6:
```math
\sum_{n=0}^N \frac{(-1)^n (x-6)^n}{(6)^{n+1}}$$
```
To put this series into the polynomial form, i.e. $\alpha_0 +\alpha_1x+\alpha_2x^2+\dots$, we must at every 'n' (starting from 0) expand the $(x-6)^n$ bracket using the binomial formula, and multiply by the constants. Then store in an array these $\alpha_i$'s such that for each 'n' in the series we have an array, which we then add together to complete the sum.
### Example ###
We wish to compute for 'n' up to 2:
```math
\sum_{n=0}^2 \frac{(-1)^n (x-6)^n}{(6)^{n+1}}
```
The function ```array(2, 6, taylor)``` will iterate over ```taylor(n,6)``` for $n=0,1,2$, creating the arrays as follows:
```math
\frac{(-1)^0 (x-6)^0}{(6)^{0+1}} = [\alpha_0]
```
```math
\frac{(-1)^1 (x-6)^1}{(6)^{1+1}} = [\beta_0, \beta_1]
```
```math
\frac{(-1)^2 (x-6)^2}{(6)^{2+1}} = [\gamma_0, \gamma_1, \gamma_2]
```
Final array computed in ```array()``` function:
```math
[\alpha_0+\beta_0+\gamma_0, \beta_1+\gamma_1, \gamma_2]
```
