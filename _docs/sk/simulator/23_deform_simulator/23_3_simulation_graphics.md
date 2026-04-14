---
lang: sk
title: "23.3. Simulation Graphics"
---

# 23.3. Simulation Graphics

While the simulation is running, the second most recent saved step can be viewed (See Fig. 23.3.1.). Many different variables can be viewed such as plastic strain, plastic strain rate, temperature and many more under Monitor tab. Simulation Graphics ![]({{ '/assets/icons/simulator_icons/mo_simulation_graphics_icon.jpg' | relative_url }}) can be opened from GUI main by clicking on ![]({{ '/assets/icons/simulator_icons/mo_simulation_graphics_icon.jpg' | relative_url }}) icon, under Simulator ![]({{ '/assets/icons/simulator_icons/gui_simulation_graphics_button.jpg' | relative_url }}) option or under Preview tab ![]({{ '/assets/icons/simulator_icons/open_simulation_graphics_label.jpg' | relative_url }}) option (see Fig. 23.3.2.)

In Simlation Graphics under Step view tab (next to Monitor tab), user can do post processing for the saved steps in database using available post tool under Step view tab as shown in Fig. 23.3.3.

Even user can see the Message file under Simulation Message tab and Log file under Simulation Log tab. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image001.jpg' | relative_url }})

Simulation graphics window

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image002.jpg' | relative_url }})

Simulation Graphics under Preview tab

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image003.jpg' | relative_url }})

Step view tab in Simulation Graphics

There are also four additional ways in which to monitor a simulation those are,

  * Use the Process Monitor to determine the current step number.

  * Read the message file to determine the current step number and iteration information.

  * Open the simulation in the Post-Processor. During a simulation the database file is renamed to FOR003 and is renamed back to the original database file name upon remeshing and stopping/completion.

  * Depending up on the frequency of the steps saved in the database, it is recommended to opt for saved steps display rather than the current step.

For more information related to state variable plot Refer chapter 4.5.2. State Variables and for Graphical options Refer [6.2. Integrated Manufacturing Process Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/) and 4.2. Graphical Display.

**Object mode** : Option used to select objects and object display mode in simulation graphics display. (See Fig. 23.3.4.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image004.jpg' | relative_url }})

Object mode window

**Related Topics:**

[Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/)

[Pre-Processor](/docs/sk/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)

[Post-Processor](/docs/sk/post_processor/post_processor_mainpg/)
