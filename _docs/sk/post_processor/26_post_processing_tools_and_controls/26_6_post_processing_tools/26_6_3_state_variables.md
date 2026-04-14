---
lang: sk
title: "26.6.3. State Variables"
---

# 26.6.3. State Variables

  * Different State variable types

  * Display options

  * State variables settings 

  * Controls Settings

  * Scaling

  * Color cut -off

  * Deflection settings

  * Coordinates

  * Rectangular and Cylindrical co-ordinates

  * User Defined

  * Local (material axis) 

  * Mapping****

  * Allowable Value ratio

  * Reference

  * Tool wear settings

  * Strain - Total

  * Relative Velocity

Some of the most commonly used state variables like Total displacement ![]({{ '/assets/icons/post_icons/mo_disp_sv_icon.jpg' | relative_url }}), Total Velocity![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}), Effective strain ![]({{ '/assets/icons/post_icons/mo_strain_sv_icon.jpg' | relative_url }}), Effective strain rate ![]({{ '/assets/icons/post_icons/mo_strain_rate_sv_icon.jpg' | relative_url }}), Effective stress![]({{ '/assets/icons/post_icons/mo_eff_stress_sv_icon.jpg' | relative_url }}), Temperature ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) and Damage ![]({{ '/assets/icons/post_icons/mo_damage_sv_icon.jpg' | relative_url }}) shortcut icons can be used to view contour plot for the objects displaying on the graphics window. ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }}) (Clear State Variable) icon can be used to clear the selected state variable for the objects.

More state variables can be accessed by using the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (State variables setup) icon (see Fig. 26.6.3.2.) State variables are grouped under different categories which are, ![]({{ '/assets/icons/post_icons/mo_analysis_icon.jpg' | relative_url }}) (Analysis), ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformation), ![]({{ '/assets/icons/post_icons/mo_thermal_sv_icon.jpg' | relative_url }}) (Thermal), ![]({{ '/assets/icons/post_icons/mo_heating_sv_icon.jpg' | relative_url }}) (Heating), ![]({{ '/assets/icons/post_icons/mo_micro_sv_icon.jpg' | relative_url }}) (Microstructure), ![]({{ '/assets/icons/post_icons/mo_diffn_sv_icon.jpg' | relative_url }}) (Diffusion), ![]({{ '/assets/icons/post_icons/mo_prop_sv_icon.jpg' | relative_url }}) (Properties), ![]({{ '/assets/icons/post_icons/mo_user_sv_icon.jpg' | relative_url }}) (User) and ![]({{ '/assets/icons/post_icons/mo_postprocssing_sv_icon.jpg' | relative_url }}) (Thermomechanical) and these can be accessed using icons as shown in Fig. 26.6.3.1.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image001.jpg' | relative_url }})

State variable groups

In order to plot state variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), the variable and the component of the variable must be selected (See Fig. 26.6.3.2.). Also one of the scaling types: global (min/max of all objects for all simulation steps), local (min/max of all objects for the particular step) and user-defined (which defaults to the global values) must be selected. For user-defined, the min/max values can be entered in the input fields provided to the right of the window. Then the type of contour (line/shaded/vector) and the class of objects to be plotted can be selected and finally specific objects can be selected by toggling them on/off in Object Tree. Clicking on the ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button plots the state variable in the current viewport.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image002.jpg' | relative_url }})

State variables window

**Different State variable types**

The following state variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) can be plotted in the MO Post:

**Analysis variables**

**[2D]:**

  * Minimum distance

  * Thickness

**Tool wear:**

  * Interface temperature

  * Sliding velocity

  * Interface pressure

  * Wear rate

  * Wear depth (total)

  * Tool life (no. of parts)

  
**[3D]:**

  * Minimum distance

  * Contact time

  * Folding angle

  * Surface expansion ratio

  * Surface area

  * Thickness

  
**Tool wear:**

  * Interface temperature

  * Sliding velocity

  * Interface pressure

  * Wear rate

  * Wear depth (total)

  * Tool life (no. of parts)

  * Worn Geometry

  
**Deformation [2D, 3D]:**

  * Coordinates

  * Damage

  * Damage Nodal

  * Displacement

  * Density

  * Strain effective

  * Strain nodal

  * Strain total

  * Strain rate

  * Stress

  * Stress nodal

  * Velocity

  * Relative Velocity

  * Back stress

  * Normal pressure

  * Rotation angle

  * Force

  
**Thermal [2D, 3D]:**

  * Temperature

  * Diffusion Bonding

  * Nodal heat

  * Heat flux

  
**Microstructure [2D, 3D]:**

  * Volume fraction

  * Grain Model

  
**Hardness**[2D, 3D]:****

  * Hardness

  * Cooling time

  * Cooling rate

**Diffusion [2D, 3D]:**

  * Dominant Atom

  * Atom flux

  
**Heating [2D, 3D]:**

  * Voltage

  
**Properties [2D, 3D]:**

  * Material

  * Material axes

  
**User [2D, 3D]:**

  * FEM User nodal variables

  * FEM User element variables

  * Post user variables

  * Custom variable

  
**Thermomechanical [2D,3D]:**

  * Thermomechanical node variables

  * Thermomechanical element variables

**Additive Manufacturing [3D]**

  * Normal Density

  * Layer ID

**Display options**

Different contour plot display options like Line, Shaded, Solid, MinMax, Vector plot, Iso surface Elemental contours are available for the applicable state variables. The contour plot settings can also be varied by using ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) (settings) button at the bottom of the state variables window.

  * **Line contour [2D, 3D]** : Plots the state variable selected as a line contour.

  * **Shaded contour [2D, 3D]** : Plots the state variable selected as a shaded contour.

  * **Solid Contour [2D, 3D]** : Shows the state variable with each element shaded with a constant color with very discrete color transitions of the color bar. This makes it easy to extract values from each element and to visualize low and high value regions.

  * **Elemental Contour [2D, 3D]** : Shows the state variable with each element shaded with a constant color with very smooth color transitions of the color bar. This makes it easy to visualize low and high value regions.

  * **Vector Plot [2D, 3D]** : This plots variables as vector quantities, i.e. with a scale and a direction. Only certain variables are applicable to be plotted in this manner such as velocity and displacement. For controlling vector size, shape and density of vector plot, please refer section State variables settings - Vector.

  * **Iso-surface [3D]** : Iso-Surface is a surface that represents points of a constant value. This plot type shows the plane along which a particular value of state variable is constant within object. Also for Iso-Surface properties please refer section State variables settings - Iso-Surface.

  * **Min/Max Plot [3D]** : This plot type shows only the minimum and maximum values of the defined variable on the workpiece.

**State variables settings**

**[2D,3D]** : This provides the options to vary the Contours, Vectors and Iso surface state variable display types settings. This (Settings) button is located at the bottom of the State variables window.

  
**Contours settings** : Contour settings are used to vary the Title, Label, Shaded contour settings, Line contour settings and Min/Max plot size ratio. 

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image003.jpg' | relative_url }})

Contour - Title type settings window

  * **Title** : The user can change the title by activating User-defined title, change the color and font as shown in Fig. 26.6.3.3.

  * **Label** : The user can change the number format to the set significant decimal value, change the color for line contour and font. Also can turn on /off the Min/Max value Display. (See Fig. 26.6.3.4. )

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image004.jpg' | relative_url }})

Contour - Label type settings window

  * **Shaded** : Use can select the Color bar type and the # of values.( See Fig. 26.6.3.5.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image005.jpg' | relative_url }})

Contour - Shaded type settings window

  * **Line:** Use can control the Line contour color, number of lines, Thickness and style (see Fig. 26.6.3.6.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image006.jpg' | relative_url }})

Contour - Line type settings window

  * **Min/Max Plot** : User can control the size of Min/Max plot using size ration option as shown in [Fig. 26.6.3.7.](26_6_3_state_variables.htm#Fig_26_6_3_7_Contour__Min/Max_plot_type_settings_window)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image007.jpg' | relative_url }})

Contour - Min/Max plot type settings window

**Iso surface settings [3D]** : Iso surface settings are used to vary the number of Iso-surfaces and values of the Iso surface plot. After Iso surface plotting for any state variable, user can select the settings button and vary the Number of iso surfaces and even the values of the iso surface planes using the Value sliding bar as shown in Fig. 26.6.3.8. The modified settings can be saved as default settings by selecting the Set as default checkbox.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image008.jpg' | relative_url }})

Iso Surface state variable display type settings window

  
**Vector settings** : Vector settings are used to vary the vectors type, sampling ratio, body length, thickness, head type and head scaling. 

  * **General:** The user can change the vector type to constant size or variable size and can also change the sampling ratio under General option as shown in Fig. 26.6.3.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image009.jpg' | relative_url }})

Vector general display properties window

  * **Body** : The user can change the vector body thickness and can also change minimum and maximum length under Body options as shown in Fig. 26.6.3.10.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image010.jpg' | relative_url }})

Vector body display properties window

  * **Head:** The user can change the Head type and can also scale under Head option as shown in Fig. 26.6.3.11.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image011.jpg' | relative_url }})

Vector head display properties window

**Controls Settings**

  
**Scaling [2D, 3D]** :

  * **Local (current step)** : There is a different minimum and maximum value for every step. This provides better resolution for a single step, but will cause colors to shift over multiple steps, making it difficult to track the evolution of variables. (See Fig. 26.6.3.12.)

  * **G******lo** bal (all steps)**: The same minimum and maximum value will be used for every step. This makes it easier to track evolution of a variable over several steps, but sacrifices resolution on a single step. (See Fig. 26.6.3.12.)

  * **Global (user defined)** : The same minimum and maximum value will be used for every step, which the user can define. This is particularly useful for state variables exhibiting small regions with extreme values. Resolution of the remaining area may be lost because of auto-scaling to an extreme peak. Resetting the maximum and minimum values to more reasonable values will wash out the peak values, but give much better resolution to intermediate values. (See Fig. 26.6.3.12.)

  * **Object Limits** : The Object Limits allows the user to set different minimum and maximum values for different objects. This is only activated for line contours. (See Fig. 26.6.3.12.)

  * **User Variables** : User defined variables allows one to plot any user defined variable in the post-processor. (See Fig. 26.6.3.12.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image012.jpg' | relative_url }})

State variable Control - Scaling properties window

  
**Color cut -off** : 

**[2D ,3D]** Color cutoff can be activated by turning on Cutoff Min and Cut off Max check boxes and defining the range. The region for the Cutoff range can be viewed when ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button is clicked and this region can be saved as a custom region using "Save as custom region" button (See Fig. 26.6.3.13.) so that user can view other state variables distribution within this region. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image013.jpg' | relative_url }})

Defining Color Cutoff

  
In Below Fig. 26.6.3.14. in left side viewport Effective Strain state variable is plotted using User type scaling with Min: 0.00 and Max: 2 value without defining color cutoff and in Right side viewport Effective Strain state variable is plotted using User type scaling for Min: 0.00 and Max: 2 value and with Color cutoff function. We can observe that in right viewport where Color cutoff is used system displays only the regions of the object that are within the cutoff range.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image014.jpg' | relative_url }})

Color Cutoff function

  * **Control tab other options [2D,3D]** : Histogram: It plots the histogram of a state variable distribution at the particular step.

  * **Exclude rigid zone** : General velocity solution can be a combination of rigid and deforming velocity fields. For models like shape rolling or ring rolling, most of the workpiece stays in rigid zone with a velocity field. To see pure deforming velocity field in the deforming zone, this feature can be used.

  * **None decrease** : <Text to be added>

  * **Custom region** : This is used to select a particular region on the object to study. After checking this checkbox user needs to select the interested region of study by clicking on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Define) button next to checkbox. Then in graphics window left side palette will display the options to select the nodes of the interested region. In DEFORM-V12, "Selected node only" functionality can be accessed using "Custom region". In older versions user can plot the selected region in Shaded type display only, from DEFORM-V12, selected region display is extended to solid shading. 

**Deflection settings**

**[2D, 3D] :** The user can scale the deflection using slider bar or by changing the values as shown in Fig. 26.6.3.15. and Fig. 26.6.3.16.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image015.jpg' | relative_url }})

Deflection window For 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image016.jpg' | relative_url }})

Deflection window For 3D

The user can hide or show the reference object boundary and can also change its color as shown in Fig. 26.6.3.17.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image017.jpg' | relative_url }})

Deflection - Reference option for 2D

**3D** : The user can also change the transparency of the reference object by activating the Use transparency and sliding the sliding bar as shown in Fig. 26.6.3.18.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image018.jpg' | relative_url }})

Use transparency Deflection window

**Coordinates**

  * **Rectangular and Cylindrical co-ordinates** : 

**[3D]** : There are currently two types of coordinates systems for which stress, strain and strain rate components can be viewed: Cartesian (rectangular) and Cylindrical. Cartesian coordinates is the default setting, however the Coordinates button in the display properties window allows the user to switch to Cylindrical Coordinates (only in 3D, See Fig. 26.6.3.19.). Clicking the Coordinates tab brings up a window that allows the user to select the cylindrical coordinates. The user needs to define by z-axis for the cylindrical coordinates. This axis is defined through a single point on the z-axis and one vector direction. User can use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to calculate the Center and Z 'direction value parameters. This works for contour plots and for point tracking. The cylindrical coordinates won't be viewed until the user selects either a stress, strain or strain rate components.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image019.jpg' | relative_url }})

Cylindrical coordinates properties window

**[2D]:** **Cartesian or rectangular coordinates** is the default setting for 2D DB. Which is having the R,Z,Theta and RZ components for the Axi-symmetric and Torsion geometry types, for Plane strain and Plane stress having only X,Y and XY components. (See Fig. 26.6.3.20. )

  * **User Defined [2D, 3D]** : 

This coordinate system can be used to plot variable components in any direction.

**[2D]** : (Only for Plane strain and Plane stress) By using this user can select the required axis angle from the current axis to plot the variables on that axis. (See Fig. 26.6.3.20. )

If user plot the User defined axis1 component then entering the angle 0 or 180 or 360 will plot the X component of the variable, changing this to 90 or 270 will plot the Y component of the variable.

If user plot the User defined axis1-2 then entering the angle 0 or 180 or 360 will plot the XY component of the variable, changing this to 90 or 270 will plot the -XY component of the variable.

**[3D]** : By using this user can select the axis for which user want to plot the variable in the two rows provided. (See Fig. 26.6.3.21. )

If user plot the User defined axis1 component then enter the 1 in the 1st row X cell and 1 in the 2nd row X cell will plot the X component of the variable, similarly for Y and Z components.

If user plot the User defined axis1 component then enter the 1 in the 1st row Y cell and 1 in the 2nd row Z cell will plot the YZ component of the variable, similarly for XY and ZX components.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image020.jpg' | relative_url }})

User defined coordinates properties window for 2D with SV window highlighted with user defined axis state variables

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image021.jpg' | relative_url }})

User defined coordinates properties window for 3D with SV window highlighted with user defined axis state variables

  * **Local (material axis)**

**[2D, 3D] :** When user uses local material axis, the variables will be plotted with respect to each element local material axis. From state variable window local material axis implemented state variables can be accessed as shown in below Fig. 26.6.3.22.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image022.jpg' | relative_url }})

SV window highlighted with local material axis state variables

**Mapping**

**[2D, 3D]:** A special post-processing variable can be “**Mapped** ” from a state variable stored in a database via a look-up table (See Fig. 26.6.3.23.). The user selects a state variable on the tree, then defines a name for the new User Defined State Variable and supplies cross reference values.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image023.jpg' | relative_url }})

SV Mapping window

**Procedure to define the Mapping** :

  * Click on![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

  * Select a State variable

  * Click on Mapping tab

  * Turn on Use SV Mapping check box

  * Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add new user defined state variable

  * Define name for the user defined state variable

  * Click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) and define the look up table.

  * Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image024.jpg' | relative_url }})

State Variable Mapping Example

**Allowable Value ratio**  
This is a kind of safety plot, with ratio numbers indicating in which regions that are exceeding safety limit as per defined table data for given variable like max principle stress. For example if we define safe max principle stress value at different temperatures in the table, this should plot this ratio on the object with regions/values over 1.0 indicating the regions over the safety limit. (See Fig. 26.6.3.25.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image025.jpg' | relative_url }})

Allowable Value ratio

**Reference**

**[3D]:** User can now define reference frame to calculate minimum distance. When user selects Minimum Distance state variable, Reference tab is added in State variable page (See Fig. 26.6.3.26.). In Reference tab user can Turn on Reference surface check box by clicking on button and select the Reference frame, then system uses this reference frame for calculating the minimum distance (See Fig. 26.6.3.27.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image026.jpg' | relative_url }})

State Variable - Reference Tab

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image027.jpg' | relative_url }})

Reference Surface picking option

**Tool wear settings**  
Tool wear rate and Tool life analysis variables can be reviewed with different tool wear model parameters and tool life criteria (See Fig. 26.6.3.29. and Fig. 26.6.3.30.). Changing the tool wear rate parameters will instantaneously affect wear rate calculation. These can be accessed from Tool wear tab, but these will activate when respective analysis state variables are selected as shown in Fig. 26.6.3.28.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image028.jpg' | relative_url }})

State variable Tool wear options

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image029.jpg' | relative_url }})

Tool wear rate settings

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image030.jpg' | relative_url }})

Tool life settings

**Strain -Total**  
User can customize the display of the Total strain variable by turning off the respective components under Strain -Total tab as shown in below Fig. 26.6.3.31. Strain-Total tab is activated when user selects Strain-Total State Variable in State Variable dialog.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image031.jpg' | relative_url }})

Strain Total selection option window

**Relative Velocity**  
Relative velocity allows the user to plot the relative velocity with reference to other objects. User can select either translation or Rotation to observe the respective relative motion and from the reference pull down menu user can select the reference object with respect to which the relative velocity to be plotted, see below Fig. 26.6.3.32.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image032.jpg' | relative_url }})

Relative velocity selection option window
