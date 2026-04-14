---
lang: sk
title: "10.6. Grain Data"
---

# 10.6. Grain Data

10.6.1. Avrami Model  
10.6.2. Texture - controlled model

![]({{ '/assets/images/pre-processor/10_material_data/10_6_grain_data/10_6_image001.jpg' | relative_url }})

Grain Recrystallization model setting window

Numerous phenomenological models have been published in the area of grain modelling, and controversies exist on the definitions of various recrystallization mechanisms. To accommodate these models, DEFORM has chosen the most popular definitions and generalized equation forms. (See Fig. 10.6.1.) In each time step, based on the time, local temperature, strain, strain rate, and evolution history, the mechanism of evolution is determined, and then the corresponding grain variables are computed and updated.

## **Avrami Model**

The Avrami equation describes how solids transform from one phase (state of matter) to another at constant temperature. It can specifically describe the kinetics of crystallization ( Fig. 10.6.2.). For more information refer [chapter 10.6.1. Avrami model](/docs/sk/pre_processor/10_material_data/10_6_grain_data/10_6_1_avrami_model/). 

![]({{ '/assets/images/pre-processor/10_material_data/10_6_grain_data/10_6_image002.jpg' | relative_url }})

Avrami Grain Material model window

## Texture - controlled model

![]({{ '/assets/images/pre-processor/10_material_data/10_6_grain_data/10_6_image003.jpg' | relative_url }})

Texture- controlled material model window
