---
lang: en
title: "Appendix VI: Part is deforming but strain does not accumulate"
---

# Appendix VI: Part is deforming, but strain does not accumulate

There is a relatively common situation in DEFORM in which a part deforms, but effective strain remains identically zero, and other variables, such as stress, behave strangely.

The problem is common when the strain rate is very small, and is related to a value known as “limiting strain rate”

**_What is limiting strain rate?_**

The rigid-plastic formulation in DEFORM is based on stresses developed in an element due to deformation. In the rigid-plastic model, if an element is not plastically deforming, the stress in the element is ambiguous. However, for good convergence, a consistent stress is required.

To improve convergence, DEFORM uses a value known as Limiting Strain Rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) to identify rigid, or nearly rigid regions of the part and to calculate flow stress in regions with near zero deformation rates.. Generally, the relationship between flow stress and strain rate is non-linear, as defined by the flow stress law. At values below the limiting strain rate, the flow stress-strain rate relationship is assumed to be linear between 0 and ![]({{ '/assets/images/appendices/appendix_vi_part_is_deforming/sigma_epsalon_l.jpg' | relative_url }}) where ![]({{ '/assets/images/appendices/appendix_vi_part_is_deforming/sigma_epsalon_l.jpg' | relative_url }}) is the flow stress at the limiting strain rate.

Elements whose strain rate is below the limiting strain rate are considered to be “rigid” for the purposes of the calculation. They do not accumulate strain, and the reported effective stress may be quite low.

**_How is limiting strain rate calculated?_**

Limiting strain rate is maintained as a fixed ratio of the “Average Strain Rate”.The ratio is defined in the preprocessor [Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/) and is normally 100:1. At strain rates below [LMTSTR](/docs/en/keyword_documentation/l/lmtstr/), the flow stress is calculated based on a linear fit from 0,0 to the flow stress at [LMTSTR](/docs/en/keyword_documentation/l/lmtstr/).

At each deformation time step, the average strain rate of all deforming elements is calculated, then the limiting strain rate is recalculated from this updated value.

Strain and damage are not incremented for elements with a strain rate below [LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)

**Why does this cause a problem?**

If the strain rate of every element in the simulation is less than the limiting strain rate, the average strain rate will never be recalculated and the limiting strain rate will also never be recalculated. This is necessary for simulations with rigid body movement, such as may occur in the early stages when a part is settling in a tool. However, it causes problems when deformation is slow enough that elements deform, but remain below the limiting value. It is possible to see quite large deformations in a part while the part displays no strain.

**How is this problem resolved?**

For simulations where the deformation rate will be slow, the average and limiting strain rate must be redefined before the start of the simulation. The values are set under the Properties dialog for each plastic object. Average strain rate can be estimated from V/L, where V is the tool velocity, and L is the characteristic deforming length of the part. 

Limiting strain rate should generally be defined as 1/100 of average strain rate.

The exception is simulations where the rigid portion of the workpiece will see a high sustained stress below the yield stresses. Examples include machining simulations and free extrusions. In these cases, the rigid region may tend to “creep” under sustained stress. A limiting strain rate 5 orders of magnitude smaller than the average strain rate should be used in these cases.

_**Average strain rate calculation for different conditions:**_

[LMTSTR](/docs/en/keyword_documentation/l/lmtstr/) is maintained as a constant ratio to the average strain rate [AVGSTR](/docs/en/keyword_documentation/a/avgstr/). After each solution step, [AVGSTR](/docs/en/keyword_documentation/a/avgstr/) is recalculated as the non-weighted average of all deforming elements. [LMTSTR](/docs/en/keyword_documentation/l/lmtstr/) is then recalculated based on the ratio initially defined in the preprocessor.

For typical simulations, a 2 order of magnitude ratio between AVGSTR & LMTSTR is appropriate (i.e. AVGSTR = 1, LMTSTR = 0.01)

For simulations with extremely low strain rates, the average and limiting strain rates should be calculated based on AVGSTR = V/h where V is the characteristic forming velocity (i.e. die or punch speed) and h is the characteristic workpiece height. LMTSTR = 0.01* AVGSTR.

For simulations involving a large constant stress on non-deforming regions of a workpiece, the rigid zone may “drift” slightly, causing small but potentially significant errors. For these types of simulations, a 5 order of magnitude ratio (i.e. AVGSTR = 1, LMTSTR = 1e-5) Typical cases include FREE EXTRUSION and MACHINING.

![]({{ '/assets/images/appendices/appendix_vi_part_is_deforming/image0001.jpg' | relative_url }})

Comparison between Flow stress and Limiting Strain Rate

**Related Topics:**

[Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)
