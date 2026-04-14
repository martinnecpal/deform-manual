---
lang: en
title: "WINATM (2D)"
---

# WINATM

|  (Object data – 2D  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

WINATM Object, Iwin, Ndata, Crbtype, SRCtype, SpdType

Velx, Vely

Iwin(1)…Iwin(Ndata)

Followed by Data

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Iwin |  Heat exchange window index |  None  
Ndata |  Number of data pairs for window coord. |  None  
Crbtype |  Type of atom content definition  =**0** Constant =**1** Function of time |  None  
SRCtype |  Type of surface reaction coefficient definition  =**0** Constant =**1** Function of time =**2** Function of atom content =**3** Function of time and atom content |   
SpdType |  Speed type  =**0** or**1** Constant =**-n** Following object |  0  
  
DEFINITION  
---  
WINATM specifies the diffusion window and window parameters for an object.  
  
REMARKS  
---  
Keyword Format Example Velx, Vely Win(X1) Win(Y1) Win(NdataX) Win(NdataY) NumCrb Time(1) Atom(1) Time(Ndata) Atom(Ndata) Numtim NumAtm Time(1) Tim(Ndata) C(1) C(Ndata) Atm(1) Atm(Ndata) SRC(1) SRC(Ndata) Applicable Simulation Modules: Microstructure Applicable [Simulation Mode](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Transformation  
  
RELATED TOPICS  
---  
[Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): [Diffusion windows](../../pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions.htm#14.4.1._Diffusion_with_the_environment_BCC_) Keywords: [ENVATM](/docs/en/keyword_documentation/e/envatm/), [ACVCOF](/docs/en/keyword_documentation/a/acvcof/), [LOCATM](/docs/en/keyword_documentation/l/locatm/)
