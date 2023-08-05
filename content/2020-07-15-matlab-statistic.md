---
title: "Matlab Statistic"
date: "2020-07-15"
tags: ["Matlab"]
image: ""
gradients: ["#4e54c8", "#8f94fb"]
---

## Binomial Distribution
```matlab
x  = 74		%% amount of x
y = 80 		%% round up of x in tenths
fail = 0.09	%% failrate
1 - binocdf( x - 1, y, 1 - fail )		%% at least

%% [ E(X) , Var(X) ]
[ x, v ] = binostat( x, 1 - fail )
xSquared = v + x^2			%% from Var(X) = E(X^2) + E(E)^2
y = 50*x - 0.4*xSquared		%% Give equation
```

## Poisson Distribution
```matlab
a)
mu = 3.5 	%% mean
v = 4	%% value
1 - poisscdf( v, mu )

b)
e = mu
v = e 	%% poison distribution
%% Var(Y) (v) = E(Y^2) (ySquared) - E(Y)^2 (e)^2
ySquared = v + (e)^2
x = 11 + 11*e + ySquared
```

## Exponential Distribution
```matlab
a)
e = mu
v = e 	%% poison distribution
%% Var(Y) (v) = E(Y^2) (ySquared) - E(Y)^2 (e)^2
ySquared = v + (e)^2
x = 11 + 11*e + ySquared

mu = 68		%% mean
%% X ~ E(mu)
fun = @(x) (1/mu)*exp(-x/mu)		%% Exponential distribution equation
q = integral( fun, 0, 25 )		%% probability value

b)
atLeast = 7 	%% probability at least value
total = 19		%% out of total given value
p = 0.361		$$ probability
1 - binocdf( atLeast - 1, total, p)
```

## norminv
```matlab
%% P(X > C) = y
norminv(1 - y)

%% P(X <= C) = y
norminv(y)

%% P(-C < X < C) = y
%% 2 | P(X > C) | = y
abs(norminv( (1-y)/2 ))
```

### normcdf and founding n in xBar-mu/(sd/sqrt(n))
```matlab
mu = 14         %% mean
sd = 0.175      %% standard dev
n = 75          %% probabilty value
%% X ~ N( mu, std/sqrt(n) )
%% P( lower < X < upper )
%% P( (lower-mu)/(std/sqrt(n)) < X < (upper-mu)/(std/sqrt(n)) )
lower = 13.99
upper =  14.01
z1 = (lower-mu)/(sd/sqrt(n))
z2 = (upper-mu)/(sd/sqrt(n))
p = normcdf(z2) - normcdf(z1)
ans = 1 - p

b)
l = 1 - 0.08 		%% change the percentage
m = (1+l) / 2
n = norminv(m)
p = upper - mu		%% usually take upper value
b = ((sd*n)/p)^2
```

```matlab
mu = 14         %% mean
sd = 0.175      %% standard dev
n = 75          %% probabilty value
%% X ~ N( mu, sd/sqrt(n) )
xBar = n*mu		%% exceeding value
max = 600       %% max value
normcdf( (xBar-max)/(sd*sqrt(n)) )

b)
exceed = 1 - 0.03           %% percentage to not exceed
p = norminv(1 - exceed)
xBar = p*(sd/sqrt(n)) + mu
upper = xBar*n
```

## Simple histogram
```matlab
x = [...]
quantile(x,[0 0.25 0.50 0.75 1])       %% Five point summary
mean(x)                                %% average
std(x)                                 %% standard dev
var(x)                                 %% Variance
histogram(x)        %% histogram to determine modal, skew and outliers
```
## Estimators
$$X$$ = It is unbiased but not consistent
$$\frac{X_{1}+X_{2}}{2}$$ = It is unbiased but not consistent
$$\frac{2X_{1}+X_{2}}{2}$$ = It is biased but not consistent