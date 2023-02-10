# ClemsonParkingSensor
Project for 2023 CUHackit

Found at: https://stevenlam505.github.io/ClemsonParkingSensor/


Inspiration

The parking situation at Clemson has grown to be a serious problem ever since the COVID-19 lockdown. The number of students on campus has increased significantly without appropriate increases to the infrastructure. As a result, parking for commuting students always takes a significant amount of time, so this project hopes to combat this problem.

What it does

The project is a sensor system to be installed at a parking space. The occupancy data of the parking space (so multiple parking spaces in a real parking space) is fed from the microcontrollers to a database. This is fed to a 3d model of the parking lot that is updated in real time to show which parking spaces are available, which students can see on the website. The front end is independent of the sensors so these can be replaced by anything based on needs.

How we built it

Arduino microcontrollers are used for the ultrasonic sensors to record distance data. Then, this sensor data is fed into a python script that forwards the information into a CockroachDB database, hosting using Amazon Web Services. This information is fed into a Unity 3d model and an html webpage to display the parking information and show some statistical data about the parking lot.

Challenges we ran into

The hardest part was getting the various parts of the design to properly interface with one another. Arduino to Python, Python to CockroachDB, CockroachDB to Unity, and CockroachDB to AWS were all connections that needed to be made and troubleshooted. In addition, SQL and Python were languages that we needed to learn on the fly, which also required some research and documentation use.

Accomplishments that we're proud of

Obviously, we were able to overcome the challenges that we ran into, which was a proud accomplishment. In particular, we are happy that we effectively delegated the work amongst ourselves and worked in an organized manner to make each individual part the best it could be. link

What we learned

We learned also sorts of useful knowledge about AWS, Python, Arduinos, Unity, and SQL. We also got some good experience with some basic idea-generating processes.

What's next for Clemson Parking Space Tracker

Hopefully, the design could be extrapolated into a lower-cost solution that is more efficient, and possibly actually used by Clemson University. We'd also like to implement more robust viewing of the 3d model, more parking lots, and support for connecting more sensors per microcontroller.
