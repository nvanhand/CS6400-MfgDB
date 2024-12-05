# CS6400-MfgDB

The following was created by Team 19 for the CS 6400 Final Project in Fall 2024. 

## Background and Purpose
The Advanced Manufacturing Pilot Facillity (AMPF) at Georgia Tech is a multi-lab makerspace and testing ground for manufacturing research projects. The space includes several top-of-the-line machines, as well as experimental cells designed by graduate students.  Historically, much of the facillity's research activities have been individual, with the lineage of experimental work primarily coming from student mentorship relationships. However, there is significant interest in capturing long-timescales data wherein many experiments are stored for analysis in bulk. Entities such as NIST, Oak Ridge National Lab, General Electric, and others have been forerunners in envisioning systems for experimental data storage, while tools exist in the traditional manufacturing space such as data historians. This project seeks to provide a proof of concept for the AMPF as to how one machine cell might store long term data and how a database system might help with analyses, with recommendations for how the work could be expanded to suit a multi-user, multi-machine, environment.  

## Definitions
Each **machine** produces a **build** which may be considered the discrete output of a machine process. The machine process may be an additive, subtractive, or otherwise transformative process. I

## Data Sources
The EOS M280 is a commerical laser powder bed fusion printer. It is capable of creating 3d printed metal parts by iteratively rolling thin layers of fine metal powders and melting them in programmed patterns to build up a part layer by layer. The process is best known for its capability to print high resolution, however, it has parameters which can affect the final print quality. As such, the machine is heavily sensorized. The AMPF M280 has two cameras, machine logging, and power sensing. Further details are elaborated in the preprocessing folder. 


## Contents
This repository contains four sections 0. Data Preprocessing, 1. Relational DB, 2. Graph DB, and 3. GUI. To replicate the results given in this repository, the folders should be invoked in order.