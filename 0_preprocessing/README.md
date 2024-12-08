
The following elaborates on the data sources and preprocessing steps. 

## Experiment Logs
The file "BuildDocumentation.xlsx" is a raw log file that users for the machine use to compile all of their experiments. A general template was created by prior students, however, the log file has no enforcement or formal record keeping. The dataset is over multiple years, but analysis was limited to those which were most consistent in formatting to simulate a well controlled system. The logs are cleaned, organized, and compiled through the buildStandardization.ipynb file and exported to a table in clean_BuildDocumentation.xlsx. From this, we also seperate out the powder information. Tracking powder usage allows manufacturer specific flaws. 

## Sensors 
Sensors.csv is a particularly made file to record the information of sensors. This was collected from sensor documentation and manually compiled into a targeted list of relevant information. The file and subsequent table allows for the unique entitities responsible for data collection to be identified. 

### Cameras
Each camera is triggered at the beginning and end of each layer. The current system writes the image to a specific path on a local fileshare. In each build, there may be up to tens of thousands of images, depending on the size of the designed build. These paths were recovered by scraping the file share for the file paths, which resulted in the eos_cam.json. These observations are parsed in cam_parser.ipynb and translated into a format suitable for bulk loading. The camera observations become rows in the SensorData table. The observing sensor is referenced from the sensor list - notably, camera 1 and camera 2 have unique attributes, which may be relevant to a user looking to use these images. 

### Laser DAQ
The part is built through  is the programmed voltage across the machine laser in additive 
