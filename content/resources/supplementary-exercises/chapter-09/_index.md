---
weight: 9
bookFlatSection: false
title: "Chapter 9"
description: "Extending constraint-based approaches"
---

# Chapter 9: Extending constraint-based approaches

1. After deleting a gene from a metabolic model, you decide to use MoMA to find the new flux distribution using the function quadprog in MATLAB. The command you have to enter is :-
{{< katex display>}} x = quadprog(H, f, A, b, A_{eq} , b_{eq}) {{< /katex >}}

     Similar to the case in *linprog*, A and b are null vectors and {{< katex >}}A_{eq} = S{{< /katex >}} and {{< katex >}}b_{eq} = 0{{< /katex >}}. What are the values of `H` and `f` that you would pass?

    a. {{< katex >}}H = -c; f = []{{< /katex >}}  
    b. {{< katex >}}H = 0.5* v^{T} I v; f = -v_w^{T} v {{< /katex >}}  
    c. {{< katex >}}H = I ; f = -v_w {{< /katex >}}  
    d. None of these  
    
   **Ans: c**
 
2. Which of the following statements are true about ROOM?

    a.  ROOM minimizes the number of significant flux changes from the wild type  
    b.  ROOM minimizes the {{< katex >}}L_{2}{{< /katex >}} norm of the flux difference from the wild type  
    c.  ROOM provides accurate flux predictions of the metabolic steady state after adaptation  
    d.  ROOM provides more accurate transient metabolic states following perturbation  
    **Ans: a, c**
    

3. Which of the following statements are correct?

    a.  Extreme pathways (EP) are an independent subset of Elementary Flux Modes (EFM)  
    b.  EP can be decomposed into the linear combinations of EFM  
    c.  EFM can be decomposed into the linear combinations of EP  
    **Ans: a, c**  
    

4. Pick the correct statement which explains the inherent assumption of the standard steady-state 13C-MFA
    
    a.  The cells are assumed to be under metabolic steady-state, and sampling is done during the isotopic non-steady state.  
    b.  The cells are assumed to be in a dynamic metabolic state, and sampling is done during the isotopic non-steady state.  
    c.  The cells are assumed to be in a dynamic metabolic state, and sampling is done once the isotopic steady-state is achieved.  
    d.  The cells are assumed to be under metabolic steady-state, and sampling is done once the isotopic steady-state is achieved.  
    **Ans: d** 