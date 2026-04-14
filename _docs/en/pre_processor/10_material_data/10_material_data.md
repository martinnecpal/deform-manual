---
lang: en
title: "10. Material Data"
---

# 10\. Material Data

The material properties window can be accessed by clicking the material list (See Fig. 10.1.).

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image001.jpg' | relative_url }})

Material list page in Operation tree

The material properties dialog is shown in Fig. 10.2. In order for a simulation to achieve a high level of accuracy it is important to have an understanding of the material properties required to specify a material used in DEFORM. The properties required are dependent on the physical effects being simulated in DEFORM. The material properties that the user is required to specify is a function of the material types that the user is utilizing in the simulation. This section describes the material data that may be specified for a DEFORM simulation.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image002.jpg' | relative_url }})

Material Properties page

**The different data sets are:**

  * [Plastic Data Definition](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_plastic_data/)
  * [Elastic Data Definition](/docs/en/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)
  * [Thermal Data Definition](/docs/en/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)
  * [Diffusion Data Definition](/docs/en/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/)
  * Dislocation Data Definition
  * [Grain Data Definition](/docs/en/pre_processor/10_material_data/10_6_grain_data/10_6_grain_data/)
  * [Hardness Data Definition](/docs/en/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/)
  * [Elec/ Mag Data Definition](/docs/en/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/)
  * [Transformation Definition](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/)
  * Coarsening Data Definition
  * Texture Data Definition
  * [Miscellaneous Data Definition](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data/)

This chapter discusses the manner in which to define each data set, and for which type of simulation each of these is required.

The DEFORM material library contains several hundred data sets. Nearly all materials contain Plastic (flow stress), elastic and thermal data. Depending on the intended application, the material data may also include microstructure related data.

The user should confirm that the material selected from the library is appropriate for the process they intend to model.

**Phases and mixtures (MSTMTR) [MIC]**  
Material groups can be classified into two categories, Regular and Mixture. “Regular” materials are appropriate for modeling most metal processing operations, including most forming, cutting, or stress analysis problems. “Mixture” materials ([MSTMTR](/docs/en/keyword_documentation/m/mstmtr/)) are used when a phase transformation is to be modeled in the simulation. The transforming material is modeled as a “mixture” of its constituent phases. For example, carbon steel might be modeled as a mixture of Austenite, Pearlite, Bainite, and Martensite. If a mixture material is defined, transformation rules should be defined which govern the transformation of one phase into another.

**Multiphase:** To add multiple Phases we need check the Mixture material check as shown in Below Fig. 10.3. Using ![]({{ '/assets/icons/pre_icons/mo_add_phase_button.jpg' | relative_url }}) option we can add new phases and using ![]({{ '/assets/icons/pre_icons/mo_remove_phase_button.jpg' | relative_url }}) option we can remove the added phases to the material.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image005.jpg' | relative_url }})

Adding Phase for Mixture material

**Create a New Material** ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})**** is used to define new material, after selecting this button new material adds into the Material list. By left mouse button double click in material list material name can be renamed and its properties must be defined in the respective tabs (Described in the further sections like Plastic data, Elastic data, etc.).

**Delete Current Materia****l**![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }})** **will delete the current material selected in the material list.

**Import Material from a file** ****![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})**** is used to import the material data from the DB or Key file into the problem setup.

**Load Material from library** **![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})** using this user can load material from DEFORM material database. (See Fig. 10.4.) Based upon the application user can select cold forming, hot forming, Heat treatment and Machining operations check boxes. Also other filters like material standard, unit system and user/system library will make the selection of material easier.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image003.jpg' | relative_url }})

Load material from library window

**Save Material data to a file**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }})****is used to save the material data from DEFORM problem setup in key file format. This material data can be used by importing back into the other problem setups.

**S****ave Material data to library![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }})** is used save the user defined material into the deform user library. While saving in the user needs to save under the some category and can also give the application based filters and the comments (see Fig. 10.5.).

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image004.jpg' | relative_url }})

Save Material in User Material library window

**Copy Properties** ![]({{ '/assets/icons/pre_icons/mo_copy_properties.jpg' | relative_url }}) is used to copy the regular material properties like plastic, elastic, thermal etc. from one material to other while creating/defining the material data. (See Fig. 10.6.) In this dialog source and destination for copying the properties and which properties to be copied must be selected.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image006.jpg' | relative_url }})

Copy properties window

**Convert Units** ![]({{ '/assets/icons/pre_icons/mo_convert_units_button.jpg' | relative_url }}) is used to convert the current selected material from material list from SI to English or English to SI or user can use any other multiplication factor. (See Fig. 10.7.) Selecting the ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) button will display the multiplication factors for converting from SI to English, similarly for ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}), selecting the ![]({{ '/assets/icons/pre_icons/mo_convert_button.jpg' | relative_url }}) button will convert and close the conversion window. This conversion table can be saved using ![]({{ '/assets/icons/pre_icons/mo_save.._button.jpg' | relative_url }}) button and can also edited by using wordpad/notepad and loaded back **UNITCONV.DAT** file using button.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image007.jpg' | relative_url }})

Material Unit converter window

**Material Assigning for object**

Below Fig. 10.8. shows the material window. User can assign required material from the list or can import and save from file or library. User can also add new material, even edit and delete the material in list from object material window. 

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image008.jpg' | relative_url }})

Material window

Once after adding material click on ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) button, material window will open as shown in Fig. 10.9.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image009.jpg' | relative_url }})

Edit material window

Related Topics:

[10.1. Plastic Data Definition](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_plastic_data/)

[10.2. Elastic Data Definition](/docs/en/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)

[10.3. Thermal Data Definition](/docs/en/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)

[10.4. Diffusion Data Definition](/docs/en/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/)

10.5. Dislocation Data Definition

[10.6. Grain Data Definition](/docs/en/pre_processor/10_material_data/10_6_grain_data/10_6_grain_data/)

[10.7. Hardness Data Definition](/docs/en/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/)

[10.8. Elec/ Mag Data Definition](/docs/en/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/)

[10.9 Transformation Data Definition](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/)

10.10. Coarsening Data Definition

10.11. Texture Data Definition

[10.12. Miscellaneous Data Definition](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data/)
