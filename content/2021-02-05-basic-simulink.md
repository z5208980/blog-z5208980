---
title: "Basic Simulink"
date: "2021-02-05"
tags: ["Matlab", "Simulink"]
gradients: ["#4568DC", "#B06AB3"]
---

## Simulink
requires us to use block diagrams. Block are just like actions you take for your system. A block can be a sine_wave, differentiate, integral, dropdown.

So our example is trying to simulate a sine wave and display it. To do so, we first need to open simulink. Either click the *simulink* button or type the following in the cl.

```
simulink
```

To **save** a model, simply save as with the extension `.slx`

## Library Browser
The button *Library Browser* is used to access all the ‘blocks’ for the system. Since we are creating a sine wave, we can get a sine block, located at `‘Simulink’ > ‘Sources’ > ‘Sine Wave’`. Drag and drop onto the model.

**Mux** (Multiplexer) allows us to view two or more signals in one graph or ‘scope’.

**Gain** basic like a multiply.

### Block Parameters
You can adjust setting for the block by double clicking the placed block in the model.

Some common blocks and properties that are adjusted are, **Sine Wave**
- frequency
- amplitude
**Scope**
- number of input ports (int to detemine the number of inputs)
**Sum**
- number of signs (no. of + is no. of inputs)

### Exporting to Matlab
Now that the model is built, we should get this to the real world application or through Matlab. To do so, we use the block **To Workplace**. Change the variable *name* to whatever you like.

Once that is done, then automatically in Matlab, in workspace there should exist the variable of your model.

### User input
This is where we get to write a script for the model so that users can input data for the model. Important thing about using use inputs is that the **contsant** block needs to be in variable such as, `x`, or `X`; declaring a variable like in coding. After saving the model as an `.slx` we use matlab’s script to access the model.

*Just a side note that scripts are `.m` files.*

In the script we need to run the model when we need to use it.

```matlab
propmt = 'Enter temperature in Celcius: '
x = input(propmt)	% input user
sim(model) 			% loading the model with any variables declared at the top
```