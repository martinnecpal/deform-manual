---
lang: en
title: "52. Introduction to DOE"
---

# 52\. Introduction to DOE

DOE (design of experiments) is a systematic approach to investigation of a system or process. A series of structured tests are designed in which planned changes are made to the input variables of a process or system. The effects of these changes on a pre-defined output are then assessed using DOE Post. DOE environment in DEFORM can be used for,

  * Sensitivity analysis to address variabilities / uncertainties in processing conditions, material data and boundary conditions.

  * Model “multiple operations” and run multiple jobs for sensitivity study.

  * Statistical analysis and probabilistic modeling.

Typical structure explaining the role of the DOE in process or product design in Multiple operation environment is as shown in Fig. 52.1.

![]({{ '/assets/images/doe_and_optimization/52_doe_study/image001.jpg' | relative_url }})

Role of DOE in Process or Product design

DOE can be performed only after a nominal simulation is completed. DOE simulation is carried out in three stages those are Preprocessing, Simulating and Postprocessing the DOE samples.

DOE Preprocessor is where user needs to define the DOE variables, range of fluctuations/uncertainty of study variables, total sample size or sampling method. Using unified control program DOE Job samples can be simulated by one click in batch mode. DOE post provides user friendly tools to investigate the input parameters and output response from multiple samples simulation results at specified operations and locations.

**Related Topics:**

[52.1. DOE and DOE Output Operation Setup](/docs/en/doe_and_optimization/52_doe_study/52_1_doe_and_doe_output_operation_setup/)

[52.2. DOE Simulation Running and Monitoring](/docs/en/doe_and_optimization/52_doe_study/52_2_doe_simulation_running_and_monitoring/)

[54.1. DOE Post Processor](/docs/en/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/)

[2D DOE Lab1](/docs/en/labs/doe_labs/2d_doe_lab/2d_doe_lab1/)
