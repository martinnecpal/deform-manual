---
lang: sk
title: "26.6.17. Data Extraction"
---

# 26.6.17. Data Extraction ![]({{ '/assets/icons/post_icons/mo_data_extraction_icon.jpg' | relative_url }})

  
[2D, 3D]:This utility in the post processor allows user to extract any model variable for a given object, at a given step in to a text file. (See Fig. 26.6.17.1.). From DEFORM -V12, user can extract State Variable data based on co-ordinate system that is used for plotting state variable in State Variable page. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_17_data_extraction/image001.jpg' | relative_url }})

Data extraction window

**Data Type** : Information can be written out in an ASCII format to an output file. The following items listed below can be extracted. For meshed objects, these are typical state variables, and for rigid die objects, load stroke data can also be extracted.

**Object Data** : Furthermore, specific keywords from Object data can be selected, as well as the objects that the data is to be extracted for. 

**Output** : The information can be extracted to either a single file or separated into multiple files. 

**Steps** : Single steps or all of the steps can be selected. To select a specific step, highlight the step in the step scroll down menu towards the right side of the screen. If 5 or 6 steps are desired and every step in the database is not desired, use control button on keyboard and select required steps in the data extraction window step list.

**Files** : The information can be extracted to one file or multiple files. A good time to implement this option is when information for more than one step is desired. Data can be written to one file, or multiple files labeled name0001.DAT, name0002.DAT etc. 

**Data File** : The name of the file, by default it is labeled DEFORM.DAT. This file can be renamed, or browse can be used to find an existing file.

**Extract** : Once the desired information has been selected, press the extract button to extract the information.
