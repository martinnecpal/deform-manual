---
lang: sk
title: "RSEDEF (3D)"
---

# RSEDEF

|  (Object data - 3D)  
---|---  
_Update History:_ V11 - RSEDEF has been introduced. |  Last updated on : 13-08-2013  
  
* * *

RSEDEF Object, Ndata

Option, Cutoff_strain_rate, Rigid_percent, Mass_density, Gravity, Vx, Vy, Vz

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of data |  8  
Option |  RSE option 1 =**0** Disable RSE =**1** Check RSE activation for first step =**2** Check RSE activation for every step |  1  
Cutoff_strain_rate |  Cutoff strain-rate |  0.0  
Rigid_percent |  Minimum percentage of rigid region |  0.0  
Mass_density |  Mass density |  0.0  
Gravity |  Gravity |  0.0  
Vx |  Unit direction vector for gravity in X dir. |  0.0  
Vy |  Unit direction vector for gravity in Y dir. |  0.0  
Vz |  Unit direction vector for gravity in Z dir. |  0.0  
  
DEFINITION  
---  
RSEDEF specifies the control parameters for RSE solver.  
  
REMARKS  
---  
In RSE solver, the cutoff strain-rate is first determined in a conservative manner based on the current and previous solution behavior/distribution. And then, RSE determines possible rigid regions based on these information and mesh topology. After that, it takes only the candidate deforming regions for full computation and the remaining regions for simplified computation associated with a rigid body motion. Depending on Option flag setting, RSE activation may be examined in the following different manners. For Option=0, RSE solver will be turned off. For Option=1, the possibility of RSE solver will not be examined once the RSE solver was deactivated at the previous step. For Option=2, the possibility of RSE solver is examined at every step. (Recommended for processes like cogging) Cutoff_strain_rate is automatically determined in a conservative manner based on the current and previous distributions of strain-rate, strain, the rate of plastic work, the gradient of strain-rate, and so on. The limiting stain-rate is used for initial filtering to reduce the amount of computation mentioned above. In general, it is not simple to select the best cutoff strain-rate in views of solution accuracy and simulation time for a given problem unless a user understands the nature of problem very well in addition to the knowledge of rigid-plastic FEM. However, if there is a user-defined cutoff value, the above procedures are by-passed.  Rigid_percent indicates the minimum percentage of rigid region for activation of RSE solver. Mass_density is the mass density of material. The unit of mass density must be Kg/mm3 for SI system and slug/in3 for English system. When it is specified other than zero, it will generate the inertia force which is originally designed for initial positioning problems. Gravity is the acceleration of gravity and Vx,Vy,Vz are the direction cosines of the gravity. The unit of gravity must be mm/s2 for SI and in/s2 for English. It is important that Mass_density and Gravity must be used only for complicated initial positioning problems like turbine blade forging. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic)  
  
RELATED TOPICS  
---  
Boundary Constraints: [Deformation](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)\- [Advanced BCC](../../pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions.htm#14.2.10._Advanced_deformation_BCC)
