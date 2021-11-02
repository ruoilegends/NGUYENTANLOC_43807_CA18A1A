"""
Author: Nguyen Tan Loc
Date: 22/10/2021
Problem:
 Where are module variables, parameters, and temporary variables introduced and
initialized in a program?
Solution:
Module variables
 • Module variables are those that can be accessed anywhere if the module in which they contain is imported.
 • The module variables of any module can be viewed by using dir() method.
 • First the module must be imported and then the function dir(module_name) generates a list that contain module variables of the respective module which was imported.
 • Module variables should be introduced at the beginning of the module outside of all the functions.
 • Module variables can be initialized anywhere where they are used. Sometimes the module variable of one module are initialized in the other module.

 Parameters
  • Parameters are also known as arguments which serve as inputs to a function.
  • Parameters are of two types. They are actual parameters and formal parameters.
  • Actual parameters are those that are provided in the function call and formal parameters are those which are present in the function definition.
  • Parameters are introduced in the function or method header.
  • Parameters do not get any value in it until the function is called.
  • In case of default parameters, they are initialized in the function definition itself.

Temporary variables
• Temporary variables are those which are introduced inside a function.
• These variables are created at the time execution of the functions and are destroyed soon after the function's execution.
• These can be accessed only inside a function. • Temporary variables can be initialized anywhere inside a function.
• These are mostly used in the logic where swapping is involved.
    ....
"""