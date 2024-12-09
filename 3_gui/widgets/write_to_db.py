import sqlite3
import os
from dateutil.parser import parse as dateparse


# Table headers
headers = ['BuildID', 'Nickname', 'Operator', 'DatePrinted', 'Customer',
       'BuildPlateType', 'BuildPlateID', 'FileLocation', 'ParameterFileName',
       'Successful', 'TotalPartVolume', 'PrintTime', 'BeginningHopperLevel',
       'EndHopperLevel', 'MinCharge', 'MaxCharge', 'PartHeight',
       'PowderHeightUsed', 'PowderHeightUsed_Per_PartHeight',
       'BuildDescription_Purpose', 'NotesOnBuild', 'LaserHours',
       'EstimatedPowderNeeded', 'PreBuildNotes', 'PostBuildNotes',
       'RecoaterType', 'RecyclingState', 'DosingBoost', 'GasFlowVoltage',
       'BuildShiftX', 'BuildShiftY', 'PowderID']

mapping = {'Operator': 'Operator', 'DatePrinted': 'Date',
        'BuildDescription_Purpose': 'BuildDescription',
        'PowderID': 'Material',
        'ParameterFileName': 'ParameterFile',
        'FileLocation': 'BuildFolder',
        'BuildPlateType': 'BuildPlateType',
        'Customer': 'Customer',
        'Nickname': 'BuildNickname',
        'BuildID': 'BuildId',
        'Successful': 'Successful?'
    }
    

def execute_query(q, read=False):
    dbf = os.path.join(os.path.dirname(os.getcwd()), "mfgdb")
    conn = sqlite3.connect(dbf)
    cursor = conn.cursor()

    try:
        cursor.execute(q)
        if read:
            r = cursor.fetchall()
        conn.commit()
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        conn.close()
        if read:
            return r


def decompose_outputs(session):
    row = []
    for field in headers:
        if field in mapping.keys():
            row.append(session[mapping[field]])
        elif field in session.keys():
            row.append(session[field])
        else:
            row.append('')
    return row

def preprocess_outputs(bd):
    # Process build attributes to be inserted into df.  
    bd['PrintTime'] = dateparse(bd['FinishTime']) - dateparse(bd)['Date']
    bd['Date'] = dateparse(bd('Date')).date

def get_material(name):
    q = f'SELECT PowderID FROM PowderLots WHERE Material == "{name}"'
    return execute_query(q, True)[0][0]

