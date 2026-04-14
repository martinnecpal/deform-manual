---
lang: sk
title: "Appendix II : Launching the Simulation Engine from a Command Prompt"
---

# Appendix II: Launching the Simulation Engine from a Command Prompt ( Windows Only)

**Purpose:** Sometimes a new engine is given to a user for a special application that is not covered in a release version. The user can use this document to see how to run the engine without having to overwrite the current engine.

**Step 1: Place the new engine in the installation directory of DEFORM-2D being careful not to overwrite the current engine.**

When receiving the engine, it must be located in the directory where DEFORM-2D is installed. The installed engine name will be DEF_SIM.EXE, so be sure to rename the new executable to other name than any of the file available in install directory before copying to the install directory.

**Step 2: Rename a current database to the name FOR003 in the necessary problem directory.**

This is the name of the database while a simulation is running. After the simulation is completed, be sure to rename it back to it’s original name.

**Warning:**

Make sure that the simulation is finished before renaming it back or risk losing all the work. If you are unsure, rename it back to a different name than the original name. 

**Step 3: Execute the Simulation Engine**.

This is done by opening a dos prompt and changing to the directory where the problem is located. A dos prompt can be accessed by either selected a shortcut from the Start Menu or by typing cmd in the Run menu. Once the dos prompt is open, it will look like the Fig. AII.1. Let’s assume that the dos prompt starts in the C:\ directory and the problem we want to run is the "C:\Users\TESTING1\PROBLEM" directory. To navigate from the C:\ directory to the end directory type the following:

**cd “C:\Users\TESTING1\PROBLEM”**

and the current working directory will become Settings and documents/test. To then run the new version of DEFORM-2D, make sure that the file FOR003 is in this directory. After this, execute the new engine by calling the executable in the DEFORM-2D directory. An example is seen in Fig. AII.2.

![]({{ '/assets/images/appendices/appendix_ii_launching_the_simulation_engine/image0001.jpg' | relative_url }})

A new dos window

![]({{ '/assets/images/appendices/appendix_ii_launching_the_simulation_engine/image0002.jpg' | relative_url }})

Running a simulation from a dos window

**Related Topics:**

[Appendix III: Running the DEFORM in text mode](/docs/sk/appendices/appendix_iii_running_deform_in_text_mode/)

[Appendix XVII: Data Files](/docs/sk/appendices/appendix_xvii_data_files/)
