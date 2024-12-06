
# README: Neo4j Desktop Setup and Usage

## Setup Instructions

1. **Create a Local DBMS**  
   - Open the Neo4j Desktop application.  
   - Create a new local DBMS instance and set it up with your preferred credentials.

2. **Install the APOC Plugin**  
   - Navigate to the "Plugins" section of your DBMS.  
   - Install the **APOC** plugin.

3. **Add Configuration File**  
   - For your local DBMS, click on the **"Open Folder"** option and select **"Configuration"**.  
   - Place the provided `apoc.conf` file into the configuration folder.

4. **Start the Local DBMS**  
   - Start your DBMS instance to ensure the configuration changes take effect.

5. **Add Import Files**  
   - For your local DBMS, click on the **"Open Folder"** option and select **"Import"**.  
   - Place the following files into the `Import` folder:  
     - `clean_BuildDocumentation.csv`  
     - `powder_lots.csv`  
     - `eos_cam.json`

6. **Access the Neo4j Browser**  
   - Open the Neo4j Browser to interact with your database.

---

## Load Data into Database

1. Open the `Create_All.cipher` file in a text editor.  
2. Copy its contents and paste it into the Neo4j Browser query editor.  
3. Execute the script to import data from `clean_BuildDocumentation.csv`, `powder_lots.csv`, and `eos_cam.json` into your database.

---

## Example Queries

Below are some example queries to explore your data.

1. **Graph Customers with Image Nodes**  
   ```cypher
   MATCH p=()-[r:Ordered]->() 
   RETURN p
   UNION
   MATCH p=()-[r:LINKED_TO]->() 
   RETURN p
   ```

2. **Graph Customers, Their Builds, and the Powders Used**  
   ```cypher
   MATCH p1=(c:Customer)-[:Ordered]->(b:Build)
   MATCH p2=(b)-[:USES]->(p:Powder)
   RETURN p1, p2
   ```

3. **Retrieve All Builds Ordered by 'Jaime'**  
   Including Powders, Success Status, Image Files, and Build Plate Types:  
   ```cypher
   MATCH (c:Customer {name: 'Jaime'})-[:Ordered]->(b:Build)
   OPTIONAL MATCH (b)-[:USES]->(p:Powder)
   OPTIONAL MATCH (b)-[:SuccessStatus]->(s:Successful)
   OPTIONAL MATCH (b)-[:UsesBuildPlate]->(t:BuildPlateType)
   OPTIONAL MATCH (b)-[:LINKED_TO]->(f:FilesNode)
   RETURN c, b, p, s, t, f
   ```

---

## Notes
- Ensure the DBMS is running before executing any queries.  
- Double-check that `clean_BuildDocumentation.csv`, `powder_lots.csv`, and `eos_cam.json` are in the correct `Import` folder.  
- If you encounter any errors during the setup or while running queries, double-check the file locations and configurations. Failing to place the apoc.conf in config will produce errors
- For additional troubleshooting, refer to the Neo4j documentation or support channels. 

