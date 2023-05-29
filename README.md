# cross_test_files
Test files for https://github.com/galou/freecad.cross

## Installation

```bash
THIS_REPO=<path/to/this/repo>
cd ~/.local/share/FreeCAD/Macro
ln -s $THIS_REPO/fc_files/cross_macro_utils.py
ln -s $THIS_REPO/fc_files/mobile_robot.fcmacro
ln -s $THIS_REPO/fc_files/parallel_fingers.fcmacro
ln -s $THIS_REPO/fc_files/robot_0.fcmacro
ln -s $THIS_REPO/fc_files/robot_1r.fcmacro
ln -s $THIS_REPO/fc_files/robot_5r-complete.fcmacro
ln -s $THIS_REPO/fc_files/robot_5r.fcmacro
ln -s $THIS_REPO/fc_files/workcell-robot_5r-complete.fcmacro
```

## Launch

- Open `empty.fcstd` in FreeCAD
- Menu "Macro / Macros..."
- Select a macro and click on "Execute"
