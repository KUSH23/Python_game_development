from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("flappybird.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
        'include_files' : ["images/background.png", "images/bird.gif", "images/bird_wing_down.png",
                                           "images/bird_wing_up.png", "images/ground.png", "images/pipe.png",
                                           "images/pipe_body.png", "images/pipe_end.png"]

                        
    },

}

setup(
    name = "Flap and die",
    options = options,
    version = "1.0.0",
    description = 'Die',
    executables = executables
)