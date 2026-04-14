---
lang: sk
title: "Appendix XIII: Fine Points on Using Force Controlled Dies"
---

# Appendix XIII: Fine Points on Using Force Controlled Dies

AXIII.1. Objective

AXIII.2. Theory

AXIII.3. Solution

## Objective

In many simulations, force-controlled dies are used in order to simulate real-world tool loading conditions. As seen in [Appendix XII](/docs/sk/appendices/appendix_xii__modelling_of_spring_loaded_die/), these can be used in order to simulate spring-loaded dies. The purpose of this section is to explain the pitfalls that can occur while trying to simulate force-loaded dies in terms of obtaining good results and improving convergence of the solution

## Theory

In reality, there is no such thing as an ideal step function. It takes time, no matter how small, for things to change. If a sudden load is applied, there must be a time span over which things occur as a ramp function. In the case of applying a load to a deformable object, there are generally two ways in which a body may respond to a given amount of force. The body may increase its reaction load by strain hardening or increase its reaction load by strain rate hardening. In the case of a high load, the final deformed shape may be quite different than the initial shape. The problem with a step function is that over one step, the body may have to deform much to achieve equilibrium with the applied load. Also, with two different possible ways in which to react can place much pressure on the simulation engine.

## Solution

As implied with the above statement on step functions, if there are no step functions then the solution must be to use ramp functions. This is the key to getting all of these simulations using force control to converge nicely. The time step size may be very small (ideally it should be realistic to the process) but as long as the deformation is spread over an ample number of steps, a good solution will result. 

**Related Topics:**

[Movement Controls Definition-Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)
