---
weight: 5
bookFlatSection: false
title: "Chapter 5"
description: "Introduction to dynamic modelling"
---

# Chapter 5: Introduction to dynamic modelling

1. For the case where continuum of molecules cannot be approximated, rate of reaction is proportional to:  
a. reactant concentrations  
b.  product concentrations  
c.  reactant partial pressures  
d.  probability of collision of reactants  
**Ans: d**

2. In Hill’s equation, which is given as:
 {{< katex >}}v =\frac{v_{max}S^n}{k'_m+S^n} {{< /katex >}}, what does  {{< katex >}}n >1 {{< /katex >}} indicate?  
    a. Competition  
    b. Cooperation  
    c. Deactivation  
    d. None of these  
    **Ans: b**

3.  A and B are two equations defined as follows, based on the two Euler methods:  
(A) {{< katex >}}x_2  = x_1  + f(x_1,t_1  )h{{< /katex >}}  
(B) {{< katex >}}x_2  = x_1  + f(x_2,t_2  )h{{< /katex >}}  
If I say that the equation (B) is (i) implicit and can be solved using (ii) Newton-Raphson method, choose the option to which you agree.  
    a. (i) is true and (ii) is true  
    b. (i) is true and (ii) is false  
    c. (i) is false and (ii) is true  
    d. (i) is false and (ii) is false  
    **Ans: a**

4.  Solve the following ODEs using ode15s in MATLAB  
{{< katex >}}\frac{dy_1}{dt}= y_2{{< /katex >}}  
{{< katex >}}\frac{dy_2}{dt}= μ(1-y_1^2 ) y_2- y_1{{< /katex >}}  
{{< katex >}}μ = 1000,   y(t=0) = [2;0]{{< /katex >}}  
Report the value of {{< katex >}}y_1 ( t = 3000){{< /katex >}}.  
**Ans: -1.502**

5. Can you solve the above ODE system (of Q.4) with ode45?  Can you solve it when the parameter μ = 1? What do you think about the stiffness of the ODEs?  
a. The ODEs are stiff when μ = 1000  
b. The ODEs are non-stiff when μ = 1000  
**Ans: a**



