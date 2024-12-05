
The following elaborates on the data sources and preprocessing steps. 

## Experiment Logs
The file "BuildDocumentation.xlsx" is a raw log file that users for the machine use to compile all of their experiments. A general template was created by prior students, however, the log file has no enforcement or formal record keeping. The logs are cleaned, organized, and compiled through the buildStandardization.ipynb file and exported to a table in clean_BuildDocumentation.xlsx.

## Cameras
Each camera is triggered at the beginning and end of each layer. The current system writes the image to a specific path on a local fileshare. In each build, there may be up to tens of thousands of images, depending on the size of the designed build. These paths were recovered by scraping the file share for the file paths, which resulted in the eos_cam.json. 