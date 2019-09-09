import cx_Freeze
import os

executables = [cx_Freeze.Executable("flappybird.py")]
os.environ['TCL_LIBRARY'] = r'C:\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python37\tcl\tk8.6'

cx_Freeze.setup(name="FlappyBird",

                options = {
                    "build_exe" : {
                        "packages": ["pygame"],
                        "include_files" : ["images/background.png", "images/bird.gif", "images/bird_wing_down.png",
                                           "images/bird_wing_up.png", "images/ground.png", "images/pipe.png",
                                           "images/pipe_body.png", "images/pipe_end.png"]

                        }
                },

                description = "Flap and die",
                executables = executables
                )