
The gui can be initiated through running the main.py function. The gui has the following Python dependencies:

    Kivy, Plyer, Pyobjus,

Running the GUI:

    python3 3_gui/widgets/main.py

If there is difficulty running the program due to unmet dependencies, run the following:

    python3 -m pip install "plyer" " kivy[base]" "pyobjus"

For more information on installing Kivy: https://kivy.org/doc/stable/gettingstarted/installation.html


The GUI is intended as an example artifact of how the group may enforce data standards. There are 4 user screens:

1. Operator identification: from this screen, the user should be able to choose the functionality. Some beginning functionality surrounding other items including machine maintenance and automatic image taking. These features are not currently tied to tables, however, once implemented, they would make use of the date and operator info.
2. Build Info: This screen is where the user may put in the information regarding a build. Currently, input validation is not enforced, however, a user should not be able to submit a build without first inputting all the required information with conforming inputs. Another intended feature is camera selection. Although not feasible with the present sensor setup, the goal would be that the user could choose which cameras would be active. 
3. Camera screen: This screen is not functional for the purpose of this project, as providing connections to sensor servers is not possible. However, this screen is intended as live feedback as to the last image taken by the cameras. 
4. Finish Screen: This screen inputs the final info that should only be done after the builds completion. it automatically populates a finish time, and when the user clicks "Finish" the build is added to the Build table in the mfgdb. 