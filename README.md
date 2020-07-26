# remote
Remote control

Package name: Remote

Description:
1. This package provides Modbus TCP/IP communication interfaces
2. Provides interface for mapping the IO registers and coils
3. A flexible dashboard to visualise collected data

Usage:
1. To use the package install the package first
2. Create a main.py file and import all the modules
3. Provide mapping details
4. Provide node description, number and name
5. Customise dashboard capabilities
6. Set broadcasting port and run main.py file
7. Open browser on a device within the local network
8. Access all the data through the dashboard

To Do:
1. Provide access to register mapping via dashboard
2. Provide control of read/write via dashboard
3. Provide testing and assertion of different cases
4. Start and stop logging should be in this class
5. Node.display data features using streamlit interface these fuctions
6. Should be within the dashboard class and need to be inherited to node
7. Start and stop logging interfaced with buttons, but how? threading?
8. Correct logging format and access via json

Non-priority:
1. Change register map from excel to json or other accessible format
  or simply a pd dataframe
  Most people are familiar and have access to excel and hence not a big problem
  Can be removed once the register map access is given via dashboard
2. Add SIGTERM to kill all processes


Utils/Common?
1. Generate heartbeat pulse (input: register)
2. Create a standard for heartbeat pulse

Parameters to be set for a new setup
1. node_name
2. node_number
3. node_description
4. log_frequency
5. host_ip
6. host_port
7. register_map.xlsx in 'comm\mapping.xlsx'
8. Initiate log file called 'log.json'
9. Database location and name

For testing in linux systems:
1. Use the following free simulator: https://www.modbusdriver.com/diagslave.html

node@11507
node"11507
