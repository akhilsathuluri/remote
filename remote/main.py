import pandas as pd
from node import node
import camutils

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
    # Write loop_number for diagnostics
    loop_number = 0
    rq = node.client.write_registers(map['reg_pi_last_loop'], loop_number, unit=node.unit)
    # Search for trigger
    # In this case we can read


    # ----------------------------------------------------
    # Wierd register not being read error
    # ----------------------------------------------------


    trigger1 = node.client.read_holding_registers(map['reg_plc_trigger1'], 1, unit=node.unit)
    trigger2 = node.client.read_holding_registers(map['reg_plc_trigger2'], 1, unit=node.unit)
    trigger1 = trigger1.registers[0]
    trigger2 = trigger2.registers[0]
    # Handle not being able to read register (AssertionError already exists)
    print(map['reg_plc_trigger1'], ', ', map['reg_plc_trigger2'])
    print(trigger1, ', ', trigger2)
    # # print('Waiting for trigger')
    #
    # # Trigger 1 only after component seat check is verified
    # # Start cycle
    # if trigger1 == 1:
    #     loop_number = 1
    #     rq = node.client.write_registers(map['reg_pi_last_loop'], loop_number, unit=node.unit)
    #     # Read PLC model register
    #     plc_model = node.client.read_holding_registers(map['reg_plc_model'], 1, unit=node.unit)
    #     plc_model = plc_model.registers[0]
    #     # Check models
    #     ret, identified_model = check_model(plc_model)
    #     # Handle not being able to write register
    #     if ret == True:
    #         # Write model verify register
    #         rq = node.client.write_registers(map['reg_pi_model_ok'], 1, unit=node.unit)
    #         # Write model number register
    #         reg_name = 'reg_pi_model_'+str(identified_model)
    #         rq = node.client.write_registers(map[reg_name], 1, unit=node.unit)
    #     elif ret == False:
    #         rq = node.client.write_registers(map['reg_pi_model_nok'], 1, unit=node.unit)
    #         reg_name = 'reg_pi_model_'+str(identified_model)
    #         rq = node.client.write_registers(map[reg_name], 1, unit=node.unit)
    #     elif ret == 'ERROR':
    #         # To handle camera prediction errors
    #         rq = node.client.write_registers(map['reg_pi_error'], 1, unit=node.unit)
    #     else:
    #         # To handle unknown read/write or pi errors
    #         rq = node.client.write_registers(map['reg_pi_unknown_error'], 1, unit=node.unit)


# # Trigger 2 only after component seat check is verified
# if trigger2 == True:
#     loop_number = 2
#     ret = check_orientation()
#     # Handle not being able to write register
#     if ret == True:
#         rq = client.write_registers(reg_ori, 1, unit=UNIT)
#     elif ret == False:
#         rq = client.write_registers(reg_ori, 0, unit=UNIT)
#     elif ret == 'ERROR':
#         rq = client.write_registers(reg_cam_error, 1, unit=UNIT)
#     else:
#         rq = client.write_registers(reg_unknown_error, 1, unit=UNIT)
