File list
=========

- `parallel_fingers-parts.fcstd`: Part (visual and collision) for the end-effector `parallel_fingers`.
- `robot_5r.fcmacro`: Macro to generate a robot from a script. Developer tool to accelerate building a robot in case of API changes in the ROS workbench for FreeCAD. To use it, open `empty.fcstd` and run the macro.
- `empty.fcstd`: in FreeCAD, links can only be created if the document is saved, the role of the document `empty.fcstd` is to have a document in the same directory as `*-parts.fcstd` files so that the macros work.
- `robot_5r-parts.fcstd`: Parts (visual and collision) for `robot_5r`.
