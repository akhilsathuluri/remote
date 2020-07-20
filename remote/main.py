import pandas as pd
from node import node

# Initialise system
node = node.Node()
# Set node params
node.node_description = 'Pad printing machine for Husqvarna rim printing'
node.node_number = 'N1_1507'
node.node_name = 'Pad printing machine'

node.host_ip = '127.0.0.1'
node.host_port = '502'
# Load register map
map = node.load_register_map()
# Connect with slave
node.connect()

while True:
    # Search for trigger
    # In this case we can read
    trigger1 = node.client.read_holding_registers(map['reg_plc_trigger1'], 1, unit=node.unit)
    trigger2 = node.client.read_holding_registers(map['reg_plc_trigger2'], 1, unit=node.unit)
    # Handle not being able to read register (AssertionError already exists)
    # print(trigger1.registers[0], ', ', trigger2.registers[0])

    # Trigger 1 only after component seat check is verified
    # Start cycle
    # if trigger1 == True:
    #     loop_number = 1
    #     # Read PLC model register
    #     plc_model = client.read_holding_registers(reg_plc_model, 1, unit=UNIT)
    #     # Check models
    #     ret = check_model(reg_plc_model)
    #     # Handle not being able to write register
    #     if ret == True:
    #         rq = client.write_registers(reg_model, 1, unit=UNIT)
    #     elif ret == False:
    #         rq = client.write_registers(reg_model, 0, unit=UNIT)
    #     elif ret == 'ERROR':
    #         rq = client.write_registers(reg_cam_error, 1, unit=UNIT)
    #     else:
    #         rq = client.write_registers(reg_unknown_error, 1, unit=UNIT)
#
#
# # Trigger 2 only after component seat check is verified
# if trigger2 == True:
#     loop_number = 2
#     ret = orientation_check()
#     # Handle not being able to write register
#     if ret == True:
#         rq = client.write_registers(reg_ori, 1, unit=UNIT)
#     elif ret == False:
#         rq = client.write_registers(reg_ori, 0, unit=UNIT)
#     elif ret == 'ERROR':
#         rq = client.write_registers(reg_cam_error, 1, unit=UNIT)
#     else:
#         rq = client.write_registers(reg_unknown_error, 1, unit=UNIT)
