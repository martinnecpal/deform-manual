---
lang: en
title: "10.4. Diffusion Data"
---

# 10.4. Diffusion Data

10.4.1. Diffusion coefficient (DIFCOE)

  * Method 1

  * Method 2

  * Method 3

  * Method 4

  * Method 5

![]({{ '/assets/images/pre-processor/10_material_data/10_4_diffusion_data/10_3_image001.jpg' | relative_url }})

Diffusion material properties window

DEFORM allows the user to model the diffusion of the dominant atom (at this point carbon) in an object. (See Fig. 10.4.1.) The user only needs to specify the diffusion coefficient for the diffusion. For the simulation of carburizing process, normally performed before quenching,  
The Laplace equation is used for the diffusion model:

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_1.jpg' | relative_url }}) |   
---|---  
  
Note:  
Brick elements tend to produce nicer looking results than the tetrahedral elements since the mean diffusion distance is normally much smaller than the average element edge length. This will tend to make the tetrahedral results look somewhat patchy due to their generally uneven edge length.(link to be created to Brick mesh MO)

## **Diffusion coefficient (DIFCOE)**

The diffusion coefficient ([DIFCOE](/docs/en/keyword_documentation/d/difcoe/)) can be defined by the following methods:

  * **Method 1**

********Constant value for diffusion coefficient.

  * **Method 2**

****Diffusion coefficient is a function of atom content and temperature (Matrix format).

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_2.jpg' | relative_url }}) |   
---|---  
  
  * **Method 3**

Diffusion coefficient is a function of temperature and atom content (Tabular format).

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_3.jpg' | relative_url }}) |   
---|---  
  
  * **Method 4**

Diffusion coefficient is a function of temperature and atom content (Tabular format).

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_4.jpg' | relative_url }}) |   
---|---  
  
  * **Method 5**
