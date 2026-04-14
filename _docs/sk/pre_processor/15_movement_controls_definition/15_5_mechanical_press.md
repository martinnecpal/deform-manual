---
lang: sk
title: "15.5. Mechanical press"
---

# 15.5. Mechanical press

15.5.1. Crank Press  
15.5.2. Knuckle or Wedge Press  
15.5.3. Secondary Control(s)  
15.5.4. Elastic Losses

## Crank Press [2D, 3D]

The Mechanical Press type replicates the cyclic motion of a mechanical press. The parameters required to simulate the motion are the total displacement of the press (![]({{ '/assets/equations/pre_processor/15_movement_controls/dtot.jpg' | relative_url }})) relative to the current displacement (![]({{ '/assets/equations/pre_processor/15_movement_controls/dcur.jpg' | relative_url }})) and the number of strokes per unit of time ( ![]({{ '/assets/equations/pre_processor/15_movement_controls/s_dash.jpg' | relative_url }})). Using these parameters, DEFORM can compute the die speed at any point of the travel of the die. The movement direction can only be specified in the X, Y, Z, -X, -Y or -Z directions. (See Fig. 15.5.1. and Fig. 15.5.2.)

The equation to derive the die speed is:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_5_1.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image001.jpg' | relative_url }})

2D Mechanical crank press movement controls window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image002.jpg' | relative_url }})

3D Mechanical crank press movement controls window

The parameters required to specify the movement of a mechanical press are:

**Total stroke** : The total stroke for the mechanical press represents the total travel of the die from its top position to its lowest position. The unit in English units is inch and in SI units is mm.

**Strokes per second** : The Strokes per seconds represents the frequency of the press blows. This is a measure of blows per second or cycles per second.

**Forging Stroke** : This value is total remaining distance of the die in the given stroke. This value will depend on the current position of the moving die relative to the stationary die.

**Direction** : Direction is used to designate a direction in which the object's stroke will be applied.

**Connecting-Rod Length** : As seen in Fig. 15.5.3., the connecting rod length can have an influence on the speed of the ram. If the length of the connecting rod is known, it can be input as a field. If it is not known, it can left as zero and its contribution to the ram speed will not be considered.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image003.jpg' | relative_url }})

Sketch of a simple direct crank drive

## Knuckle or Wedge Press [2D, 3D]

  
In the case of less common presses, there is a capability to model their movement by defining them strictly as a velocity profile ( Fig. 15.5.4. and Fig. 15.5.5.).  
The velocity profile or **Stroke profile** is defined as an angle (in degrees) versus die stroke or position. As an angle, this has to do with the angle of rotation of a driving motor.

Stroke Profile must be positive at Top Dead Center and zero at Bottom Dead Center.

**Forging Stroke** is the (positive) distance remaining until BDC.

**Cycles/seconds** represents the frequency of the press blows. This is a measure of blows per second or cycles per second.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image004.jpg' | relative_url }})

Knuckle press movement controls window 

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image005.jpg' | relative_url }})

Knuckle press Stroke Profile

**Example Mechanical Press:**

Consider an example, case where the total displacement for a press (top-dead center to bottom-dead center) as 10 inches.

  * The first piece of information that should be determined is the movement direction of the moving die. In this case, let's consider that the moving die is moving in the Y direction. We can then set the movement direction to Y. 

  * The second piece of information is the press parameters: the speed and the displacement. These are generally fixed for the press and once determined can be saved in the press library. In this case let's assume these values to be 10 inches of displacement and a speed of 1 cycle per second (1 second to travel from TDC to BDC and back). 

  * The last piece of information to provide is the current position of the moving die at the beginning of the stroke. This can be done by using the measuring tool to determine the distance in the Y-direction of the moving tool to the BDC of the crank. It is very important that this measurement be done carefully as it will affect the final height of the part and will affect the final load of the process. In this case, if the moving die begins at 9 inches into the stroke, the initial position will be to set the current die stroke to (0, -9). This means that the moving die has moved already 9 inches downward and needs to travel an additional 1 inch downward, which is nothing but the forging stroke.

## Secondary Control(s)

The type of control will depend on the type of movement specified. In the case of a mechanical press and screw press (as seen in Fig. 15.5.6. and Fig. 15.5.7.) the only control is based on load. In the case of a hammer, there are no secondary controls since the only manner in which to stop is to run out of energy. In the case of a hydraulic press, it can stop based on the load or a minimum velocity.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image006.jpg' | relative_url }})

2D Secondary controls for object movement

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image007.jpg' | relative_url }})

3D Secondary controls for object movement

## Elastic Losses

The stiffness of a press or a hammer can be defined in this dialog. (See Fig. 15.5.8.) In the case of a press there can be stretch based on the forging load and the final distance of the press will be less by the amount of the stretch. In the case of a hammer, the compliance accounts for elastic loss of energy.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image008.jpg' | relative_url }})

Stiffness/Compliance definition for a press or a hammer

**Related Topics:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)
