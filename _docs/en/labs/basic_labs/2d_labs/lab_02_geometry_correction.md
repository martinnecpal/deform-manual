---
lang: en
title: "Lab 02 Geometry Correction"
---

# Lab 02 Geometry Correction

2.1. Creating a New Problem

2.2. Adding Forming Operation

2.3. Geometry Type

2.4. Adding Object

2.5. Geometry Editing

2.6. Saving the Problem

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear. as shown below Fig. L2.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L2.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " **Junk** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (See Fig. L2.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Junk** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0003.jpg' | relative_url }})

Problem location selection window

User can also change the Unit system (File menu selected unit system will be selected by default) and add operation by selecting from First operation pull down list and checkbox (See Fig. L2.4.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0002.jpg' | relative_url }})

Assigning problem name

## Adding Forming Operation

Multiple Operation wizard will open with new project called Junk. Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming or user can also add by drag and drop into the Operation Editor.(See Fig. L2.5.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0003.jpg' | relative_url }})

MO wizard with 2D Forming Operation

## Geometry Type

For this lab, Default Geometry Type (Axisymmetric) is OK. To setup a problem, user can select required Geometry type. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

## Adding Object

In this lab we need only one object, if already there are three objects in object list, then delete the last two objects by clicking ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) object button and keep only Workpiece object in list (see Fig. L2.6.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until workpiece geometry page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0004.jpg' | relative_url }})

Adding Objects

## Geometry Editing

In Geometry page, Click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) button as shown in Fig. L2.7. A geometry edit window will open as shown in Fig. L2.8.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0005.jpg' | relative_url }})

Geometry window

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0006.jpg' | relative_url }})

Edit Geometry window

In 2D Geometry Editor window, enter the following XYR coordinates in the table as shown in Fig. L2.9.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0007.jpg' | relative_url }})

2D Geometry Editor

Click on show vertex Number ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) icon, for the created geometry it will assign numbers at each point as shown in Fig. L2.10.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0008.jpg' | relative_url }})

Geometry with show normal vectors

Using the Box Zoom ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) icon, zoom in on the intersection between the two arcs. User can see that the endpoints of the two arcs do not meet correctly as shown in Fig. L2.11. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0009.jpg' | relative_url }})

Showing Error Geometry

Defined Geometry get displayed in Display window as shown in Fig. L2.12.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0010.jpg' | relative_url }})

Geometry in Display window

Click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button and then click on ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). The message "Geometry has been corrected" should pop up as shown in Fig. L2.13. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) for the popup. Depending upon the size of entity and default tolerance picked up by the system, some correction may need multiple attempts or increased tolerance value based on user judgement.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0011.jpg' | relative_url }})

Check geometry popup

The default correction settings worked well for this geometry, creating a small line between the two arcs.

## Saving the Problem

By selecting the File menu Export option,save a keyword file for the problem as "Junk". The data will be saved in the file Junk.KEY.

****

**Related Topics:**

[12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)
