---
weight: 10
bookFlatSection: false
title: "Chapter 10"
description: "Perturbations to metabolic networks"
---

# Chapter 10: Perturbations to metabolic networks

1. Consider the following reaction sequence and choose the correct statement(s) about synthetic and single lethals.
    {{< katex display >}}
    R1: A + B  \rightarrow C    
    {{< /katex >}}

    {{< katex display >}}
    R2: C +A  \rightarrow D  
    {{< /katex >}}

    {{< katex display >}}
    R3: B + D  \rightarrow E + F  
    {{< /katex >}}

    {{< katex display >}}
    R4: A + D  \rightarrow E + F     
    {{< /katex >}}

    {{< katex display >}}
    R5: E + F \rightarrow Biomass  
    {{< /katex >}}
    
    a.  R3 and R4 is a synthetic lethal pair  
    b.  R2 and R4 is a synthetic lethal pair  
    c.  R3 is a single lethal  
    d.  R4 is a single lethal  
    
    **Ans: a, b**
    
    
    Download the *Escherichia coli* str. K-12 substr. MG1655 model `‘iAF1260.mat’` from http://bigg.ucsd.edu/models/iAF1260. Load and analyze the model in MATLAB.

2. What is the number of essential reactions (growth rate upon deletion results in < 5% of  the wildtype growth) observed in the anaerobic `iAF1260` model?  

   **Ans: 292**
        
        
3. Perform a knockout of the Pyruvate Dehydrogenase (PDH) reaction in the anaerobic  model of `iAF1260`. What is the maximum acetate production flux of the knockout strain  (The biomass flux should at least 90% of the wildtype under anaerobic condition)?  

   **Ans: 8.26 mmol/gDW/h**  
   
   
4. Which of the following can help to identify a potential drug target for a bacterial disease affecting humans?  
    a. A gene that does not change the biomass flux of the bacterium when knocked out.  
    b. A gene that does that significantly reduces the biomass flux of the bacterium when knocked out.  
    c. A bacterial protein involved in biomass production of the bacterium and having a structure different from any human proteins.  
    d.A bacterial protein involved in biomass production of the bacterium and having a structure very similar to a human protein.  
    
    **Ans: b, c** 


5. Consider the MATLAB code:  
`[grRatio, grRateKO] = doubleGeneDeletion(model)`. 
The MATLAB command `sum(grRatio<0.05)` gives:  

    a.The sum of the growth rates that are less than 5% of wild-type growth rate.  
    b.The number of reactions for which the growth rate is 5% of wild-type growth rate.  
    c.The number of gene-pair deletions for which the growth ratio is less than 0.05.  
    d.The number of gene-pair deletions for which the growth rate of the deletion strain is less than 5% of the wild-type growth rate. 
    
   **Ans: c, d** 
