---
lang: sk
title: "TTTD (2D3D)"
---

# TTTD

|  (Inter-material data)  
---|---  
_Update History:_ v11 - New types of (9, 10, 11, and 12) MEDC, Secondary alpha lath, Ti-beta to GB alpha and Ti-beta to SP alpha have been added. |  Last updated on : 09-08-2013  
  
* * *

TTTD Mat1, Mat2, Type, ThmDirCond

(please see Remark for detail data format)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat1 |  Material number 1 |  None  
Mat12 |  Material number 2 |  None  
Type |  = **1** Diffusion data (TTT table form) Function of time, atom content, and mean stress |  None  
|  = **2** Martensitic data (TMS, TM50 table form)  
Function of atom content and mean stress |  None  
|  = **3** Diffusion data (function form) |   
|  = **4** Diffusion data (function form, f(T) is as point data) |   
|  = **5** Martensitic data (function form) |   
|  = **6** Simplified form for diffusion type |   
|  = **7** Diffusion data for recrystallization (not available in GUI) |   
|  = **8** Melting and solidification (not available in GUI) |   
|  = **9** MEDC (new in v11) |   
|  = **10** secondary alpha lath (new in v11) |   
|  =**11** Ti – beta to GB (grain boundary) alpha (new in v11) |   
|  = **12** Ti – beta to SP (side plate) alpha (new in v11) |   
|  =**-N** User routine N |   
ThmDirCond |  Thermal direction condition |  None  
|  =**0** No condition |   
|  =**1** Heating |   
|  =**2** Cooling |   
  
DEFINITION  
---  
TTTD defines the time, temperature, and transformation diagram data that are needed in a phase transformation analysis. GUI is not supported for the types of 7 and 8.  
  
REMARKS  
---  
Type 1: Diffusion data (TTT table form) function (t, c, s) TTT (time-temperature-transformation) diagram, TTA (time-temperature-austenitizing), PTT (precipitation-time-temperature) and so on are specified as a table form. The other diffusion type transformations including recrystallization are applied as this data. TTT is used for ferrite, pearlite, bainite and tempering transformations, and TTA and PTT are named for only Austenite transformation and Precipitation, respectively. The transformation start and end curves are inputted by the time in the logarithmic value at some temperature, carbon content and stress levels. In case of recrystallization and precipitation the curves depend on grain size and plastic strain, not carbon content and stress.  
  
(format)  |  TTTD Mat1, Mat2, Type(=1), ThmDirCond Kdpnd, nocurves Kdpnd- Kind of dependency Nocurves- Number of curves (max 2) =0 depends on carbon content and stress =1 depends on plastic strain and grain size if (ncurves=1) then coefficient n of Avrami eq, volume fraction of curve else volume fraction of each curve end if no atom, no stress, no temp carb 1, carb 2, .. (kdpnd=0) or pstr1, pstr2, .. (kdpnd=1) sts1, sts2, sts3 .. (kdpnd=0) or grns1, grns2, .. (kdpnd=1) temp1, temp2, .. t1, t2, (carb1, sts1, temp1, … or pstr1, grns1, temp1, …)  
---|---  
  
Type 2: Martensitic data (TMS, TM50 table form) function (c, s)

The transformation start and 50% level temperature are inputted as a table format by depending on carbon content and stress levels.

(format)  |  TTTD Mat1, Mat2, Type(=2), ThmDirCond Number of curves Number of carbon content Number of mean stresses Car1, Car2, … Sts1, Sts2, Sts3, … Temp1, Temp2 (carb1, sts1, …)  
---|---  
  
Type 3: Diffusion data (function data form)

Volume fraction ![]({{ '/assets/equations/keyword_documentation/t/zeta_1.jpg' | relative_url }}) is represented by the Avrami equation as follows:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_1.jpg' | relative_url }}) |   
---|---  
  
The power ![]({{ '/assets/equations/keyword_documentation/t/small_n.jpg' | relative_url }}) depends on the kinds of the transformation and ![]({{ '/assets/equations/keyword_documentation/t/ft_t.jpg' | relative_url }}) can be expressed by the following simplified formula,

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_2.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/equations/keyword_documentation/t/fs_m.jpg' | relative_url }}) in addition, ![]({{ '/assets/equations/keyword_documentation/t/fc_c.jpg' | relative_url }}) describes the stress and carbon content dependency of transformation, respectively as follows:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_3.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_4.jpg' | relative_url }}) |   
---|---  
  
(format)  |  TTTD Mat1, Mat2, Type(=3), ThmDirCond AT1, AT2, AT3, AT4, AT5, AT6, AT7, AS, AC1, AC2, N; coefficient  
---|---  
  
Type: 4 Diffusion data (function form, f(T) is as point data)

f(T) in the above type is specified as data points of temperature

(format)  |  TTTD Mat1, Mat2, Type(=4), ThmDirCond AS, AC1, AC2, N; coefficients Number of temperature T1, F(T1), T2, F(T2)..  
---|---  
  
Type 5: Martensitic data (function data form)

The volume fraction of diffusionless-type (martensite) transformation depended on temperature, stress and carbon content is introduced by modifying the Magee's equation as follows:

The volume fraction of diffusionless-type (martensite) transformation depended on temperature, stress and carbon content is introduced by modifying the Magee's equation as follows:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_5.jpg' | relative_url }}) |   
---|---  
  
When the martensite transformation start temperatures under carburized conditions and applied stress are given, ![]({{ '/assets/equations/keyword_documentation/t/phi2_by_phi1.jpg' | relative_url }}), ![]({{ '/assets/equations/keyword_documentation/t/phi31_by_phi1.jpg' | relative_url }}) and ![]({{ '/assets/equations/keyword_documentation/t/phi32_byphi1.jpg' | relative_url }}) can be determined ![]({{ '/assets/equations/keyword_documentation/t/phi1.jpg' | relative_url }}) and ![]({{ '/assets/equations/keyword_documentation/t/phi4.jpg' | relative_url }}) are identified, if temperatures for martensite-start TMS and for 50% martensite TM50 at![]({{ '/assets/equations/keyword_documentation/t/zeta_m.jpg' | relative_url }}) = 0 and ![]({{ '/assets/equations/keyword_documentation/t/zeta_m.jpg' | relative_url }}) = 0.5 are provided respectively.

(format)  |  TTTD Mat1, Mat2, Type(=5), ThmDirCond Psi1, si2, psi31, psi32, psi4, C0; coefficients  
---|---  
  
Type 6: Simplified form for diffusion type

The volume fraction can be evaluated by the following equation as the first approximation for diffusion type:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_6.jpg' | relative_url }}) |   
---|---  
  
(format)  |  TTTD Mat1, Mat2, Type(=6), ThmDirCond A: D: TS: TE: coefficients  
---|---  
  
Type 7: Diffusion data for recrystallization (GUI is not implemented)

The volume fraction of recrystallization is usually defined by the equation including the time for 50% recrystallization as follows:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_7.jpg' | relative_url }}) |   
---|---  
  
(format)  |  TTTD Mat1, Mat2, Type(=7), ThmDirCond B, n1, a, m, n2, Q, R; coefficients  
---|---  
  
Type 8: Melting and solidification (GUI is not implemented)

The volume fraction of solid is specified as a point data of temperatures.

(format)  |  TTTD Mat1, Mat2, Type(=8), ThmDirCond Number of temperature T1, V(T1), T2, V(T2),....  
---|---  
  
Type 9: MEDC

MEDC model is developed by AFRL in the United States to predict the microstructure evolution during continuous cooling of wrought alpha/beta titanium alloys in the two-phase field. The growth of the primary (globular) alpha during cooling is modeled using an exact solution of the diffusion equation:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_8.jpg' | relative_url }}) |   
---|---  
  
The particle radius is converted to volume fraction using the following expression:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_9.jpg' | relative_url }}) |   
---|---  
  
The intrinsic diffusion coefficients of alloying elements in beta titanium can be expressed by,

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_10.jpg' | relative_url }}) |   
---|---  
  
The parameter ![]({{ '/assets/equations/keyword_documentation/t/lamda.jpg' | relative_url }}) in Equation 8 is related to the supersaturation ( ![]({{ '/assets/equations/keyword_documentation/t/omega_s.jpg' | relative_url }})) by the following expression:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_11.jpg' | relative_url }}) |   
---|---  
  
In each calculation step, the supersaturation (![]({{ '/assets/equations/keyword_documentation/t/omega_s.jpg' | relative_url }}) ) is determined as,

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_12.jpg' | relative_url }}) |   
---|---  
  
Here, ![]({{ '/assets/equations/keyword_documentation/t/cm.jpg' | relative_url }}) , ![]({{ '/assets/equations/keyword_documentation/t/ci.jpg' | relative_url }}) and ![]({{ '/assets/equations/keyword_documentation/t/cp.jpg' | relative_url }}) represent the compositions of the matrix far from the matrix-particle interface, the matrix at the matrix-particle interface, and the particle at the matrix- particle interface respectively. For a diffusion-controlled reaction, ![]({{ '/assets/equations/keyword_documentation/t/ci.jpg' | relative_url }}) and ![]({{ '/assets/equations/keyword_documentation/t/cp.jpg' | relative_url }}) correspond to the equilibrium matrix and particle compositions respectively and they were obtained from the phase diagram. ![]({{ '/assets/equations/keyword_documentation/t/cm.jpg' | relative_url }}) considers the effect of soft impingement on the “far-field” matrix composition, and is calculated by the usual approximation derived from a mass balance:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_13.jpg' | relative_url }}) |   
---|---  
  
The input parameters of MEDC model include the beta approach curves (showing the volume fraction of beta as a function of temperature), the equilibrium chemical compositions of alpha and beta phases, and diffusivity as a function of temperature, solution temperature / initial volume fraction of alpha phase, initial alpha particle radius, and cooling rates. The initial volume fraction of primary alpha (![]({{ '/assets/equations/keyword_documentation/t/fao.jpg' | relative_url }})) is automatically computed based on the provided beta approach curve in terms of the solution temperature (the starting temperature of the cooling process). The initial particle size (![]({{ '/assets/equations/keyword_documentation/t/rao.jpg' | relative_url }})) is determined by user, generally based on the experimental data. The evolution of primary alpha volume fraction and the size are computed based on the local cooling rate during DEFORM heat transfer simulation.

If secondary alpha lath thickening model (Type 10) is defined, MEDC model is automatically coupled with secondary alpha growth model. The growth of primary alpha is terminated by the starting growth of secondary alpha.

(format)  |  TTTD Mat1, Mat2, Type(=9), ThmDirCond Ndata(=2), NCurve(=2) ConstA, ConstB (for Vanadium or Aluminum) 1,1, NTemp Chemical composition (of Valadium or Aluminum, C0) 0.00 Temp(1), Temp(2), ..., Temp(NTemp) CI(1), CI(2), ..., CI(NTemp) CP(1), CP(2), ..., CP(NTemp)  
---|---  
  
Type 10: Secondary alpha lath

A fast acting model is developed to predict the thickening kinetics of secondary alpha lath. Considering the soft impingement between the adjacent advancing laths, the thickening kinetics of a secondary alpha in a colony structure can be expressed as:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_14.jpg' | relative_url }}) |   
---|---  
  
The alpha equilibrium disolving temperature is assumed to be 980oC.

The CCT curve to describe the secondary alpha starting temperatures under various cooling rates is fitted by a fifth order polynomial equation:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_15.jpg' | relative_url }}) |   
---|---  
  
(format)  |  TTTD Mat1, Mat2, Type(=10), ThmDirCond Ndata(=10) AlphaMatNo, A_sp, Q_sp, C_sp, a5, a4, a3, a2, a1, a0  
---|---  
  
Type 11: Ti-beta to grain boundary alpha

A fast acting model is developed to predict the thickening kinetics of grain boundary alpha in Ti-6Al-4V. It is assumed that a layer of grain boundary alpha of negligible thickness develops right after the temperature drops below the beta transus. During further cooling or isothermal holding, grain boundary alpha continues to grow until the sideplate alpha starts to develop. Therefore, this type of transformation is generally coupled with Type 12 (Ti-beta to sideplate alpha). The thickening kinetics of grain boundary can be described as,

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_16.jpg' | relative_url }}) |   
---|---  
  
The CCT curves to describe the grain boundary alpha starting temperature ( ![]({{ '/assets/equations/keyword_documentation/t/tu.jpg' | relative_url }}) ) and sideplate starting temperature (![]({{ '/assets/equations/keyword_documentation/t/tl.jpg' | relative_url }}) ) under various cooling rates are fitted by a fifth order polynomial equation as follows:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_17.jpg' | relative_url }}) |   
---|---  
  
(format)  |  TTTD Mat1, Mat2, Type(=11), ThmDirCond Ndata(=14) A1, Q1, a5upper, a4upper, a3upper, a2upper, a0upper, a5lower, a4lower, a3lower, a2lower, a1lower, a0lower  
---|---  
  
Type 12: Ti-beta to side plate alpha

A fast acting model is developed to predict the thickening kinetics of side plate alpha in Ti-6Al-4V. It is assumed that the sideplate alpha starts to develop when the growth of grain boundary alpha stops. Therefore, this type of transformation is coupled with Type 11 (Ti-beta to grain boundary alpha). Considering the soft impingement between the adjacent advancing plates, the thickening kinetics of a can be described as,

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_18.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_19.jpg' | relative_url }}) |   
---|---  
  
The two CCT curves describing the starting temperature of grain boundary alpha (![]({{ '/assets/equations/keyword_documentation/t/tu.jpg' | relative_url }}) ) and that of side plate (![]({{ '/assets/equations/keyword_documentation/t/tl.jpg' | relative_url }}) ) under various cooling rates are fitted by a fifth order polynomial equation as follows:

![]({{ '/assets/equations/keyword_documentation/t/tttd_eq_17.jpg' | relative_url }}) |   
---|---  
  
(format)  |  TTTD Mat1, Mat2, Type(=11), ThmDirCond Ndata(=14) A1, Q1, a5upper, a4upper, a3upper, a2upper, a0upper, a5lower, a4lower, a3lower, a2lower, a1lower, a0lower  
---|---  
  
RELATED TOPICS  
---  
Inter-Material Data: [Transformation Kinetics](../../pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinetics_models.htm#Transformation_Kinetics_Models) Related keywords: [VOLFS](/docs/sk/keyword_documentation/v/volfs/), [VOLFC](/docs/sk/keyword_documentation/v/volfc/), [STNOUT](/docs/sk/keyword_documentation/s/stnout/)
