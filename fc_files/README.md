File list
=========

- `cross_macro_utils.py`: Common functions for the FreCAD macros in this folder.
- `empty.FCStd`: in FreeCAD, links can only be created if the document is saved, the role of the document `empty.FCStd` is to have a document in the same directory as `*-parts.FCStd` files so that the macros work.
- `robot_0.FCMacro`: Single-link robot without external dependencies.
- `robot_1r.FCMacro`: Dual-link, single-joint robot without external dependencies.
- `robot_5r-parts.FCStd`: Parts (visual and collision) for `robot_5r`.
- `robot_5r.FCMacro`: Macro to generate a robot from a script. Developer tool to accelerate building a robot in case of API changes in the ROS workbench for FreeCAD. To use it, open `empty.FCStd` and run the macro.
- `parallel_fingers-parts.FCStd`: Part (visual and collision) for the end-effector `parallel_fingers`.
- `parallel_fingers.FCMacro`: Macro to generate a gripper with parallel fingers from a script. Developer tool to accelerate building a robot in case of API changes in the ROS workbench for FreeCAD. To use it, open `empty.FCStd` and run the macro.
- `mobile_robot-parts.FCStd`: Part (visual and collision) for the mobile platform `mobile_robot`.
- `mobile_robot.FCMacro`: Parts (visual and collision) for `mobile_robot`.
- `robot_5r-complete.FCMacro`: Script to generate a 5-axis robot with a gripper as CROSS::Robot object.
- `workcell-robot_5r-complete.FCMacro`: Script to generate a 5-axis robot with a gripper as CROSS::Workcell object.
