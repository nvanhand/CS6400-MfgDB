DROP TABLE IF EXISTS Sensors;
DROP TABLE IF EXISTS SensorData;
DROP TABLE IF exists Builds;
DROP TABLE IF exists PowderLots;

CREATE TABLE PowderLots
(
    PowderID INTEGER PRIMARY KEY,
    Material VARCHAR(20), 
    Manufacturer TEXT, 
    FirstUseDate TEXT
);

CREATE TABLE Builds (
    BuildID VARCHAR(10) PRIMARY KEY,
    Nickname TEXT,
    Operator TEXT,
    DatePrinted TIMESTAMP,
    Customer TEXT,
    BuildPlateType TEXT,
    BuildPlateID TEXT,
    FileLocation TEXT,
    ParameterFileName TEXT,
    Successful TEXT,
    TotalPartVolume REAL,
    PrintTime REAL,
    BeginningHopperLevel REAL,
    EndHopperLevel REAL,
    MinCharge REAL,
    MaxCharge REAL,
    PartHeight REAL,
    PowderHeightUsed REAL,
    PowderHeightUsed_Per_PartHeight REAL,
    BuildDescription_Purpose TEXT,
    NotesOnBuild TEXT,
    LaserHours REAL,
    EstimatedPowderNeeded REAL,
    PreBuildNotes TEXT,
    PostBuildNotes TEXT,
    RecoaterType TEXT,
    RecyclingState TEXT,
    DosingBoost REAL,
    GasFlowVoltage REAL,
    BuildShiftX REAL,
    BuildShiftY REAL,
    PowderID INTEGER,
    FOREIGN KEY (PowderID) REFERENCES PowderLots(PowderID)
);

CREATE TABLE Sensors
(
    Serial INTEGER PRIMARY KEY,
    Name VARCHAR(20), 
    DataKind TEXT, 
    Model TEXT,
    Manufacturer TEXT,
    Resolution VARCHAR(15),
    Depth INTEGER
);

CREATE TABLE SensorData
(
    RecordID INTEGER PRIMARY KEY,
    BuildID VARCHAR(10) NOT NULL,
    SensorSerial VARCHAR(10),
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    FOREIGN KEY (BuildID) REFERENCES Builds(BuildID)
    FOREIGN KEY (SensorSerial) REFERENCES Sensors(Serial)
);
