---
lang: en
title: "DIFCOE (2D3D)"
---

# DIFCOE

|  (Material data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DIFCOE matr, type, (value) or (N1, N2, npt, ndim)

Temp(1)…Temp(Ndata) or Atom(1) …Atom (Ndata)

Atom(1) …Atom(Ndata) C1(1) …C1(Ndata)

DIFCOE(1) …DIFCOE(Ndata) C2(1) …C2(Ndata)

DIFCOE(1) …DIFCOE(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Matr |  Material Type |  None  
Type |  =**0** Constant =**1** f(A,T) =**2** Exponential function (=C1(T)exp((C2(T)*A)) =**3** Exponential function (=C1(A)exp((C2(A)/T)) |  None  
N1 |  Number of temperature for matrix |   
N2 |  Number of carbon content (atom) for matrix |   
Npt |  Number of temperature/atom points |  None  
Ndim |  Dimension of array (can not be changed) |  3  
  
DEFINITION  
---  
DIFCOE specifies the diffusion coefficient for carburization of the material. EXAMPLES: The format for the DIFCOE keyword file is shown for specific examples.  
  
Type 1 Example for Material 1

TEMP ( C )/ATOM (%) |  0.1 |  0.2  
---|---|---  
800 |  0.2 |  0.5  
900 |  0.6 |  0.9  
1000 |  0.98 |  0.89  
  
DIFCOE 1 1 3 4

800 900 1000

0.1 0.2

0.2 0.5 0.6 0.9 0.98 0.89

Type 2 Example of Material 1

ATOM (%) |  C1 |  C2  
---|---|---  
0.1 |  0.2 |  0.5  
0.2 |  0.3 |  0.6  
0.3 |  0.4 |  0.7  
  
DIFCOE 1 2 3 3

0.1 0.2 0.3

0.2 0.3 0.4

0.5 0.6 0.7

REMARKS  
---  
For Type 1: A is atom content and T is temperature For Type 2: C1(T) and C2(T) are coefficients as a function of temperature and A is the atom content which is extracted from the element data. For Type 3: C1(A) and C2(A) are coefficients as a function of atom content and T is temperature which is extracted from the element data. Applicable simulation types: [Microstructure](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)) Module  
  
RELATED TOPICS  
---  
Material Data: [Diffusion](/docs/en/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/) Keywords: [ENVATM](/docs/en/keyword_documentation/e/envatm/), [ACVCOF](/docs/en/keyword_documentation/a/acvcof/), [DATOM](/docs/en/keyword_documentation/d/datom/), [CRBFLX](/docs/en/keyword_documentation/c/crbflx/), [BCCCRB(2D)](/docs/en/keyword_documentation/b/bcccrb/), [BCCCRB (3D)](/docs/en/keyword_documentation/b/bcccrb_3d/)
