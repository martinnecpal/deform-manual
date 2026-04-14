---
lang: en
title: "Sheet Forming in DEFORM 3D"
---

# Sheet Forming in DEFORM 3D

1\. Theory - Anisotropy

2\. Theory - Assumed Strain Formulation

3\. Simulation Principles

4\. Example: Square cup drawing process

5\. Example: Cylindrical cup drawing process

Due to advantages in modeling thin structures, the membrane or shell element formulations are very popular in the simulation of sheet forming processes. Although shell elements represent the stress variation through their thickness effectively, they generally require special treatments for the drilling degree of freedom and the transverse shear locking to preserve the Kirchhoff or Reissner-Mindlin hypotheses. Thus, the shell formulation requires more complicated and sophisticated procedures than solid element formulations. Moreover, shell elements do not have the continuity of the thickness over the neighborhood elements. A comprehensive comparison of solid and shell elements can be found in the reference (Wriggers et. al. [1]). In the reference, the authors showed the possibility of the application of solid elements for thin shell as well as thick shell problems.

A brief coverage of the theory of anisotropy and assumed strain formulation will be presented in the following sections. After this, specific information will be provided on how to simulate accurate sheet forming applications within DEFORM-3D.

## Theory - Anisotropy

The associated flow rule with Hill'48 anisotropic yield criterion (Hill [2]) is used for consideration of initial texture property of sheet metal. The flow potential for orthotropy which conserves three symmetry planes are written in terms of the stress ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/sigma.jpg' | relative_url }})as,

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq1.jpg' | relative_url }}) |   
---|---  
  
Where

with

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq2.jpg' | relative_url }}) |   
---|---  
  
Where

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/sigma_transpose.jpg' | relative_url }})

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_11.jpg' | relative_url }})

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_22.jpg' | relative_url }})

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_33.jpg' | relative_url }})

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/2beta_12.jpg' | relative_url }})

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/2beta_13.jpg' | relative_url }})

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/2beta_23.jpg' | relative_url }})

Therefore, six independent parameters need to be defined to characterize the anisotropic hardening state.

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/sigma_o.jpg' | relative_url }}) is an equivalent stress representing the current yield surface size.

The coefficients in P can be related to the R-values (Valliappan et al. [3]). By setting (this means the principal anisotropic axis coincides the reference axis),

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_11_1.jpg' | relative_url }}); ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq3.jpg' | relative_url }}) |   
---|---  
  
The remaining parameters, ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_55.jpg' | relative_url }}),![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_66.jpg' | relative_url }}) can not be determined by the uniaxial tensile test. Generally the corresponding stresses have little effect on sheet metal forming processes, the parameters are assumed to be equal to ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/beta_44.jpg' | relative_url }}). It should be noted that von-Mises isotropic yield criterion is recovered when three R-values, R0, R45 R 90 are set to be 1. Numerical implementation of Hill’48 yield criterion is outlined below.

The additive decomposition of strain-rate into elastic and plastic parts is employed together with the normality rule,

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq4_1.jpg' | relative_url }}) ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq4_2.jpg' | relative_url }}) ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq4_3.jpg' | relative_url }}) |   
---|---  
  
where the superscripts **e** and **p** represent the elastic and plastic parts, respectively. **C** is the elasticity tensor, ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/lamda_.jpg' | relative_url }}) is the plastic strain-rate multiplier and **a** is the flow vector defined by,

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq_5.jpg' | relative_url }}) |   
---|---  
  
From Equations (4) and (5) with the consistency condition (6), the plastic strain-rate multiplier can be expressed as below:

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq6.jpg' | relative_url }}) |   
---|---  
![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq7.jpg' | relative_url }}) |   
---|---  
  
Where

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/aiso.jpg' | relative_url }})

Finally, the rate form of the constitutive equation can be written as,

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq8.jpg' | relative_url }}) |   
---|---  
  
It should be noted that the element stiffness matrix is directly related to the tangent modulus ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/cep.jpg' | relative_url }})evaluated at each integration point, which governs the convergence rate of the global iterative scheme. Thus the consistent tangent modulus is essential to keep the quadratic rate of convergence in the Newton-Raphson scheme (Simo and Taylor [4], Crisfield [5]).

## Theory – Assumed Strain Formulation

A locking-free element is essential for the robustness of the finite element method. Several versions of the reduced integration method using hourglass control techniques have made remarkable progress on this issue (Belytschko and Bachrach [6]; Hughes [7]; Belytschko et al. [8]). Li[9] and Jetteur[10] proposed a strain field modification to avoid numerical instability. This paper was based on the method proposed by Li [9]. The essential equations for the strain field description can be written as follows.

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq9.jpg' | relative_url }}) Where ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/e_o.jpg' | relative_url }}) and ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/e_h.jpg' | relative_url }}) are Constants the non-constant terms of the displacement gradient respectively |   
---|---  
  
The non-constant terms can cause undesirable locking, volumetric locking or hourglassing. To avoid these undesirable effects, the modified normal strain part, Equation (11), is assumed to be the same as Equation (12) in Equation (10).

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq10.jpg' | relative_url }}) |   
---|---  
  
Where

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq11.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq12.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq13.jpg' | relative_url }}) |   
---|---  
  
Here, the repeated index is used to denote the summation.

Possible shear locking in thin-structure analysis can be resolved on the element level by adopting the assumed transverse shear strain field (Sze and Yao [11]; Kinkel et al. [12]). The transverse shear strains are interpolated from the values evaluated at the mid-points of the element edges as below.

![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq14_1.jpg' | relative_url }}) ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/eq14_2.jpg' | relative_url }}) |   
---|---  
  
## Simulation Principles

When modeling a sheet forming process in DEFORM-3D, the following setup is recommended:

  * Brick mesh the workpiece with the “Sheet application” setting activated. Limited automatic brick remeshing is possible with such a setup.

  * Brick mesh the object with 3-4 layers of brick elements through the thickness.

  * Define the workpiece as an elasto-plastic (EP) object. The object may be defined as plastic if springback effects are not significant.

  * If the EP brick meshed workpiece only has 1-2 layers of brick elements through the thickness, then use the “Assumed strain (brick mesh)” EP formulation. See the “[Assumed](../../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#Assumed_strain_Brick_Mesh) [ strain (Brick mesh)](../../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#Assumed_strain_Brick_Mesh)” description in the “General Object Data Definition” section of the manual for more information.

  * Turn on “Adaptive contact penetration control” in the “Simulation controls > Step increment” menu.

  * Set the “Node contact update” setting, for each contact pair, to “Do not update”.

  * Use hybrid friction to allow both sliding and sticking contact.

  * Consider if anisotropy should be added for better material behavior representation.

## Example: Square cup drawing process

As an example case, consider a square cup drawing process (See Fig. SF.1). The blank is made of an aluminum alloy with the following properties:

  * Young’s Modulus: 70 GPa

  * Poisson’s ratio: 0.3

  * ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/sigma_bar.jpg' | relative_url }})

The thickness of the blank is 0.81 mm and the area of the blank is 150 mm2 x 150 mm2. The blank holder force is 19.6 kN, the punch stroke is 40 mm and the coefficient friction is 0.162. The deformation of the drawing process can be seen in Fig. SF.2 and Fig. SF.3. This simulation correlates well to experimental results as can be seen in Table 1.. The deformed shape at 40mm punch stroke is shown in [Fig. SF.3]() and the amount of draw-in along the rolling (DX), transverse (DY), and diagonal (DD) directions is compared with the average values of the measurements in Table 1. Since an isotropic yield criterion was used for this simulation, the predicted draw-in along two directions, DX and DY are almost identical in the simulation. Numerical results are well correlated with the measurement results.

![]({{ '/assets/images/applications/55_3_sheet_forming/sheet_forming_in_deform_3d/image0001.jpg' | relative_url }})

Square cup drawing process

![]({{ '/assets/images/applications/55_3_sheet_forming/sheet_forming_in_deform_3d/image0002.jpg' | relative_url }})

Square cup object (a) before deformation and (b) after deformation

![]({{ '/assets/images/applications/55_3_sheet_forming/sheet_forming_in_deform_3d/image0003.jpg' | relative_url }})

Deformed shape in square cup drawing (aluminum alloy sheet, at 40 mm punch stroke)

**Measured point** |  **Measured** |  **Simulation**  
---|---|---  
15* (DX,DY) |  5.3 mm |  5.5 mm  
15*(DD) |  3.3 mm |  3.3 mm  
40**(DX,DY) |  28.5 mm |  26.9 mm  
40**(DD) |  15.0 mm |  15.5 mm  
  
Draw-in distance. Note: * and ** denotes 15mm , 40mm punch stroke respectively

## Example: Cylindrical cup drawing process

This benchmark problem was proposed for NUMISHEET’99 (Benchmark B1-part 2), designed to explore the anisotropic aspects of sheet metal forming processes, both from experiments and numerical simulations [13]. Part I, which is omitted in this paper, refers to a deep drawn cylindrical cup with a hemispherical punch free of any localized necking or split according to the actual individual forming-limit curve. Part 2 is simulated under given a constant blank holder condition.

The typical parameters for this simulation are summarized below:

  * Blank thickness: 1.0 mm

  * Drawing ratio: 2.0

  * Constant BHF: 80 kN

  * Drawing depth : 85 mm

  * Material : DDQ (mild steel)

  * R-values: ![]({{ '/assets/equations/applications/55_sheet_forming/sheet_forming_in_deform_3d/r_values.jpg' | relative_url }})

The NUMISHEET’99 committee supplied tool geometries and material data for DDQ(mild steel). The FE model for this benchmark is shown in Fig. SF.4. The workpiece is an elasto-plastic material with the planar anisotropic yield criterion (Hill’48). The earing shapes can be obtained from planar anisotropic yield criterion and the corresponding punch travel and punch force are compared in Fig. SF.5. The amount of draw-in along the rolling (DX), transverse (DY), and diagonal (DD) directions are compared with the measurements in Table 2. The measured data is average values of three participations (B1E-02, B1E-03 and B1E-04) in NUMESHEET’99 benchmark test.

![]({{ '/assets/images/applications/55_3_sheet_forming/sheet_forming_in_deform_3d/image0004.jpg' | relative_url }})

FE model for cylindrical cup drawing

![]({{ '/assets/images/applications/55_3_sheet_forming/sheet_forming_in_deform_3d/image0005.jpg' | relative_url }})![]({{ '/assets/images/applications/55_3_sheet_forming/sheet_forming_in_deform_3d/image0006.jpg' | relative_url }})

Punch force vs. stroke curve

**Measured point** |  **Measured** |  **Simulation**  
---|---|---  
DX |  29.0 mm |  27.0 mm  
DD |  32.0 mm |  35.0 mm  
DY |  27.5 mm |  25.0 mm  
  
Draw-in distance

References:

[1] Wriggers, P.,Eberlein, R., and REESE, S., 1996, A comparison of three-dimensional continuum and shell elements for finite plasticity, Int. J. Solids Str., 33(20-22), pp.3309-3326

[2] Hill, R., 1950, The Mathematical Theory of Plasticity, Oxford Univ. Press, London, Chapter 12

[3] Valliappan, S., Boonlaulohr, P., and Lee, I. K., 1976, Non-linear analysis for anisotropic materiala, Int J Num Meth Eng. 10, 597-606.

[4] Simo, J.C. and Taylor, R.L., 1985, Consistent tangent operators for rate independent elasto-plasticity, Comp. Meth. Appl. Mech. Eng., 48, pp. 101-118

[5] Crisfield,M.A., 1987, Consistent schemes for plasticity computation with the Newton-Raphson method, Computational plasticity, part I, pp. 133-159

[6] Belytschko, T. and Bachrach. W.E., 1986, Efficient implementation of quadrilaterals with high coarse-mesh accuracy, Comp. Meth. Appl. Mech. Eng., 54, pp. 279-301

[7] Hughes, T.J.R., 1980, Genralization of selective integration procedures to anisotropic and nonlinear media, Int. J. Num. Meth. Eng., 15, pp. 1413-1418

[8] Belytschko, T., Ong. J.S., Liu, W.K. and Kennedy, J.M., 1984, Hourglass control in linear and nonlinear problems, Comp. Meth. Appl. Mech. Eng., 43, pp. 251-276

[9] Kaiping Li, 1995, Contribution to the finite element simulation of three-dimensional sheet metal forming, Ph.D thesis, MSM, Universite de Liege, Belgique

[10] Jetteur, P., 1991, A mixed finite element for the analysis of large inelastic strains, Int. J. Num. Meth. Eng., 13, pp. 229-239

[11] Sze, KY, and Yao, LQ, 2000, A hybrid stress ANS solid-shell element and its generalization for smart structure modeling. Part I-solid-shell element formulation, International Journal for Numerical Methods in Engineering, 48, pp. 545-564

[12] Kinkel, S, Gruttmann, F, Wagner, W, 1999, A continuum based three-dimensional shell element for laminated structures, Computers and Structures, 71, pp. 43-62 

[13] Gelin, J. C. and Picart, P., 1999, Proceedings of NUMISHEET’99 - The 4th international conference and workshop on numerical simulation of 3D sheet forming processes, France, September 13-17.

Related Topics:

[Material Properties](/docs/en/pre_processor/10_material_data/10_material_data/)
