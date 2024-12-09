
The following elaborates on the data sources and preprocessing steps. 

## Dependencies
Python
Python Libraries: Pandas, numpy 

# Replication

The output of clean_data can be replicated through running the buildSTandardization.ipynb script followed by the cam_parser.ipynb. The buildStandardization tool converts the raw build documentation file into the clean_builddocumentation and powder lots. Running the cam_parser converts the eos_cam.json into the sensordata.dat file. 

# Data 

## Experiment Logs
The file "BuildDocumentation.xlsx" is a raw log file that users for the machine use to compile all of their experiments. A general template was created by prior students, however, the log file has no enforcement or formal record keeping. The dataset is over multiple years, but analysis was limited to those which were most consistent in formatting to simulate a well controlled system. The logs are cleaned, organized, and compiled through the buildStandardization.ipynb file and exported to a table in clean_BuildDocumentation.xlsx. From this, we also seperate out the powder information. Tracking powder usage allows manufacturer specific flaws. 

## Sensors 
Sensors.csv is a particularly made file to record the information of sensors. This was collected from sensor documentation and manually compiled into a targeted list of relevant information. The file and subsequent table allows for the unique entitities responsible for data collection to be identified. 

## Sensor Data

Two files are given representing 5 total sensors: two cameras and 3 data aquisition channels. 

### Cameras
Each camera is triggered at the beginning and end of each layer. The current system writes the image to a specific path on a local fileshare. In each build, there may be up to tens of thousands of images, depending on the size of the designed build. These paths were recovered by scraping the file share for the file paths, which resulted in the eos_cam.json. These observations are parsed in cam_parser.ipynb and translated into a format suitable for bulk loading. The camera observations become rows in the SensorData table. The observing sensor is referenced from the sensor list - notably, camera 1 and camera 2 have unique attributes, which may be relevant to a user looking to use these images.  

### Laser DAQ
Data acquisition (DAQ) modules are common tools used in machine monitoring to track machine condition. Typically, these utilize encoders to verify the actual movement/values associated with a machine rather than the programmed one, as even if the laser is programmed to go to x1, y1, the mechanical elements that translate the laser have some degree of error. 

While our M280 does not have a DAQ module, in order to simulate the presence of one, a data set from the National Institute of Standards and Technology was utilized to provide a reasonable baseline for what that data would look like. In the data set, the DAQ module records the position of the laser in X and Y as well as the observed voltage at that position. The original dataset can be found at https://www.nist.gov/publications/process-monitoring-dataset-additive-manufacturing-metrology-testbed-ammt-overhang-part ; The powerMonitoring.ipynb script reads the original data as downloaded from NIST and transforms it into a smaller, loadable CSV format. The original data is not given due to the large size (over 1 GB of data), however, the code is still provided and should be replicable upon downloading the NIST set. 