# Elastic-Pendulum
A Vpython simulation of an elastic pendulum.

This simulation uses lagrangian mechanics to simulate how a mass on a spring, displaced from the equilbrium position, will behave. Lagrangian mechanics uses the principle of least action and conservation of energy to write differential equations for the motion of bodies in terms of variable quantites, in this case the length of the spring and the angle the spring makes with the vertical. In future, I may upload my written working in order to aquire the differential equations used in the simulation.

The differential equations obtained cannot be solved algebraically, therefore the code uses an euler method in order to solve the equations in length and angle. Vpython is then used to actually simulate the pendulum.
