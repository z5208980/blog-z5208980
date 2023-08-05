---
title: "Gradient Descent"
date: "2020-10-17"
tags: ["Machine Learning"]
image: ""
gradients: ["#ff9966", "#ff5e62"]
---


## Motivation

The purpose of training neural networks, is to minimise a **loss function**. That is the value of this loss function gives us a measure how far from perfect is the performance of our network on a given dataset.

## Gradient Descent
*Performing a descent along the direction of the gradient in a **loss** function.*

The goal of gradient descent is too found a **local minimum**. To do this, gradient descent needs to take steps. The size of the steps is called the **Learning Rate** `(η: eta)`.

### Learning Rate
- If η is too **small**, then it’ll require more training epochs.
- If η is too **large**, will converge too quickly and may skip the local minimum. Jumps too far.

### Momentum (α)
**Momentum** is used in Gradient Descent to soldier the past weights. A *momentum* factor is added before calculating the weights. It will help will smoothing out the variations.

```
δw = αδw - η dE/dw
δw (avg weights)

w = w + δw	(new weights)
```

Momentum value range at `0 ≤ α < 1` but opt for `=~ 1`. In this case, keep the learning rate low.

To use learning rate and momentum in `pytorch`

```py
optimizer = torch.optim.Adam(net.parameters(),eps=0.000001,lr=lr, betas=(0.9,0.999),weight_decay=
```