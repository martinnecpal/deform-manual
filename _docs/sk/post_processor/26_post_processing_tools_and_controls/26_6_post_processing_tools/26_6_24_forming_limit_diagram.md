---
lang: sk
title: "26.6.24. Forming Limit Diagram"
---

# 26.6.24 Forming Limit Diagram (FLD)

The formability limits in sheet metal forming set the amount of deformation that can be attained without failure by necking, fracture or wrinkling. User can select the Forming Limit Diagram (FLD) icon from the tool bar as shown in the Fig. 26.6.24.1. to define FLD related settings and view FLD curve. 

When user clicks on FLD icon ![]({{ '/assets/icons/post_icons/mo_fld_icon.jpg' | relative_url }}), it opens the Forming Limit Diagram window as shown in the Fig. 26.6.24.2. In Forming Limit Diagram window, user can define Forming limit curve along with Safety barrier, Simple tension curve (R factor) and Simple shear curve. User can plot the FLD graph with any one of these options or any combination of these options as shown in the Fig. 26.6.24.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0001.jpg' | relative_url }})

FLD Icon in tool bar

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0002.jpg' | relative_url }})

Forming Limit Diagram window

## Forming Limit Curve

The onset of necking is the most widely used formability limit in sheet metal forming, and it is generally plotted as a 'V-shaped' curve also called as Forming- Limit Curve (FLC) as shown in the Fig. 26.6.24.3. The FLC indicates the amount of deformation to be imparted to sheet metal part based on which damage can be predicted. After defining the Forming Limit Curve user can click on the plot button as shown in Fig. 26.6.24.3., then FLD graph is plotted with nodal distribution showing the nodes where fracture can occur and nodes that are safe and FLD variable is plotted over the part in display area as shown in the Fig. 26.6.24.4.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0003.jpg' | relative_url }})

Forming Limit Curve (FLC) definition

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0004.jpg' | relative_url }})

After applying the FLC curve

## Safety barrier

User can set the safety margin using Safety barrier, the Safety barrier curve is defined below Forming Limit Curve. After defining the safety barrier as shown in the Fig. 26.6.24.5. user can click on plot button, then FLD graph is plotted with nodal distribution showing nodes which are safe, nodes which are in safety margin (between barrier and FLC) and nodes at which fracture can occur as shown in Fig. 26.6.24.6. When user clicks on plot button after defining the Safety barrier then FLD state variable is plotted showing regions that are within Safe, Safe Margin and where Fracture can occur. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0005.jpg' | relative_url }})

Safety barrier definition

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0006.jpg' | relative_url }})

FLD after defining the FLC and Safety barrier

## Simple Tension Curve

Simple Tension based R factor can be defined to estimate the wrinkling trend. After defining the R factor and FLC if user clicks on the plot button, the graph is updated with simple tension curve showing the nodes that are safe from wrinkling trend and fracture, where fracture can occur, where wrinkling trend is observed as shown in Fig. 26.6.24.7. The FLD variable is plotted over the part showing the regions based on FLD graph, see Fig. 26.6.24.7.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0007.jpg' | relative_url }})

FLD after defining the FLC and simple tension curve

## Simple Shear Curve

User can turn on the Simple shear curve check box and FLC and plot the graph like Simple Tension curve showing the nodes that are safe from wrinkling and fracture as shown in Fig. 26.6.24.8. The FLD variable is plotted over the part showing the regions based on FLD graph, see Fig. 26.6.24.8.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0008.jpg' | relative_url }})

FLD after defining the FLC and simple shear curve

User can turn on all the check boxes FLC, Safety barrier, Simple tension curve and Simple shear curve and plot the graph showing the nodes that are safe from wrinkling trend, wrinkling and fracture, within safe margin, where fracture can occur, where wrinkling will occur and nodes displaying wrinkling trend as shown in Fig. 26.6.24.9. The FLD variable is plotted over the part showing the regions based on FLD graph, see Fig. 26.6.24.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0009.jpg' | relative_url }})

FLD Curve

## Thickness

When we select the thickness icon in the forming limit diagram window by default the Min. and Max thickness variable values are applied for the scaling as shown in the Fig. 26.6.24.10., user can modify the scale values and state variable plot over the forming part is updated accordingly.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0010.jpg' | relative_url }})

Thickness plot

## Damage

When we select the damage icon in the forming limit diagram window by default the Min. and Max Damage variable values are applied for the scaling as shown in the Fig. 26.6.24.11., user can modify the scale values and state variable plot over the forming part is updated accordingly.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0011.jpg' | relative_url }})

Damage plot
