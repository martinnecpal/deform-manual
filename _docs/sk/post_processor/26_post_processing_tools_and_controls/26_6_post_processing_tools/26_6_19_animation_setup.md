---
lang: sk
title: "26.6.19. Animation setup"
---

# 26.6.19. Animation setup ![]({{ '/assets/icons/post_icons/mo_animation_icon.jpg' | relative_url }})

The model results can be displayed as a continuous set of images and animation files in standard formats for presentations. These features can be accessed from the ![]({{ '/assets/icons/post_icons/mo_animation_icon.jpg' | relative_url }}) (Animation setup) icon. Animation setup settings dialogs let the users to save the images in a defined location in a specific format and resolution( See Fig. 26.6.19.1., Fig. 26.6.19.2. and Fig. 26.6.19.3..). From version 12.xx, animation can be saved in HTML, Movie and windows standard power point file format as well (See Fig. 26.6.19.3.).

Under **General** tab, user can define the File name in the File name field, using Browse button user can select the Animation saving directory. Selected path will be displayed in Directory field (See Fig. 26.6.19.1.).

After a presentation file (.pre) has been created, the "Edit in Presentation Editor" ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) button will be enabled. Clicking this button will launch the Presentation Editor. For more information related to presentation Editor refer [26.6.23. Presentation Editor](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_6_23_presentation_editor/)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image001.jpg' | relative_url }})

Animation setup general window

Under **Settings** tab user can control frame duration of “Animation start delay” , “Animation end delay”, “Operation start delay”, “Operation end delay” time and “Interval between step”. The duration is defined in “msec”.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image002.jpg' | relative_url }})

Animation setup settings window

Under **Export** tab, user can define the Image size and format to export. Image size can be set using “Image setup” option. Video size can be changed using Image size option, now Movie option with updated video format such as WMV (Version 9) and MP4 (H.264) format are available. Also using MS power point option user can export animation into .PPT file.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image003.jpg' | relative_url }})

Animation setup export window with trouble shooting message

When we generate Animation, we can observe *.pre format file is created inside the animation saved folder. User can open the “.pre” extension file using DEFORM Presentation player.   
DEFORM animation (.pre) files behave likes “flip book”. Below figure shows the format of .pre file, user can Edit the .pre file manually. PNG image of each selected step will be saved inside the Images folder.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image004.jpg' | relative_url }})

Format of .pre file

  
**Creating movie file from .pre using command prompt**  
Using existing .pre file user can regenerate movie files with the help of DEF_MOVIE.exe using command prompt. When DEF_MOVIE.EXE file is opened in Command prompt, user can observe the format as shown below. 

“ Movie file creator provided by DEFORM(TM)  
Version 12.0

DEF_MOVIE format filename1 filename2 {option} {resolution}

format movie file format  
wmv - WMV format (Legacy)  
avi - AVI format (Legacy)  
adv - Advanced format options  
filename1 input file name (*.pre)  
filename2 ouput file name (*.wmv, *.avi, *.mp4)  
{option} resolution control  
for WMV format  
1 - low resolution (320x240)  
2 - high resolution (640x480)  
for AVI format  
1 - no compression  
2 - MPG4  
for Advanced format options  
1 - WMV (version 9)  
2 - MP4 (H.264)  
{resolution}  
for Advanced format resolution  
1 - Use image size  
2 - 320 x 240  
3 - 640 x 480  
4 - 800 x 600  
5 - 1024 x 768  
6 - 1280 x 720  
7 - 1600 x 1200  
8 - 1920 x 1080 

Example to create movie file using command prompt:  
“<deform install path>\ DEF_MOVIE.exe adv spike.pre spike.wmv 1 1 “
