---
weight: 6
bookFlatSection: false
title: "Chapter 6"
description: "Parameter estimation"
---

# Chapter 6: Parameter estimation

1. Solve the following ODE in MATLAB using `ode45` and report the value of {{< katex >}}y(t=10){{< /katex >}}. Report 4 significant digits of your answer.  
{{< katex display >}}
    \frac{dy}{dt} = \frac{y+t^2-2}{t+1}; y(0) = 2
{{< /katex >}}
**Ans: 69. 25**

2. Using `fminsearch` in MATLAB, find the minimum of the following function.
{{< katex display >}}  
   f(x,y) = x^2y - 2xy^2 +3xy +4
{{< /katex >}}
       Use {{< katex >}}[-1.2, 1]{{< /katex >}} as the initial guess. Report 2 significant digits of all the values.  
    * Report the minimum value.  
    **Ans: 3.5** 
    * Report the value of x<sub>min</sub>.  
    **Ans: -1.0** 
    * Report the value of y<sub>min</sub>.  
    **Ans: 0.5**
    
3.  I have a measured set of data points as given in the following table.  
    | x     | y    |
    |:----: | :---:|
    | 500   | 0.05  |  
    | 550   | 0.1  |
    | 600   | 0.2  |
    | 650   | 0.4  |
    | 700   | 0.8  |  
    
    It is known that y and x are related according to the equation: 
{{< katex >}}y=A \exp(\frac{−B}{x}){{< /katex >}}. Which of the following values of the parameters fit the measured data points well?  

    a. A = 1000, B = 5000  
    b. A = 900, B = 4500  
    c. A = 5000, B = 5500  
    **Ans: a**
        
  