import pandas as pd
from node import node
from camutils import *

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

# Reset the entire memory block under pi's control
start_register = 50
block_length = 15
rq = node.client.write_registers(start_register, [0]*block_length, unit=node.unit)

while True:
    # Write loop_number for diagnostics
    loop_number = 0
    rq = node.client.write_registers(map['reg_pi_last_loop'], loop_number, unit=node.unit)

    # Check if PLC is reset in between
    reset = node.client.read_holding_registers(map['reg_plc_reset'], 1, unit=node.unit)
    if reset.registers[0] == 1:
        # Reset entire memory block data
        rq = node.client.write_registers(start_register, [0]*block_length, unit=node.unit)
    else:
        pass

    # Search for trigger
    trigger1 = node.client.read_holding_registers(map['reg_plc_trigger1'], 1, unit=node.unit)
    trigger2 = node.client.read_holding_registers(map['reg_plc_trigger2'], 1, unit=node.unit)
    # Handle not being able to read register (AssertionError already exists)
    print('Waiting for trigger')

    # Trigger 1 only after component seat check is verified (handled by PLC)
    # Start cycle
    if trigger1.registers[0] == 1:
        loop_number = 1
        rq = node.client.write_registers(map['reg_pi_last_loop'], loop_number, unit=node.unit)
        # Read PLC model register
        plc_model = node.client.read_holding_registers(map['reg_plc_model'], 1, unit=node.unit)
        # Check models
        ret, identified_model = check_model(plc_model.registers[0])
        # Handle not being able to write register
        if ret == True:
            # Write model verify register
            rq = node.client.write_registers(map['reg_pi_model_ok'], 1, unit=node.unit)
            # Write model number register
            reg_name = 'reg_pi_model_'+str(identified_model)
            rq = node.client.write_registers(map[reg_name], 1, unit=node.unit)
        elif ret == False:
            rq = node.client.write_registers(map['reg_pi_model_nok'], 1, unit=node.unit)
            reg_name = 'reg_pi_model_'+str(identified_model)
            rq = node.client.write_registers(map[reg_name], 1, unit=node.unit)
        elif ret == 'ERROR':
            # To handle camera prediction errors
            rq = node.client.write_registers(map['reg_pi_error'], 1, unit=node.unit)
        else:
            # To handle unknown read/write or pi errors
            rq = node.client.write_registers(map['reg_pi_unknown_error'], 1, unit=node.unit)

    # Trigger 2 only after component seat check is verified (handled by PLC)
    if trigger2.registers[0] == 1:
        loop_number = 2
        rq = node.client.write_registers(map['reg_pi_last_loop'], loop_number, unit=node.unit)
        # Check orientation of the rim
        ret = check_orientation()
        # Handle not being able to write register
        if ret == True:
            rq = node.client.write_registers(map['reg_pi_ori_ok'], 1, unit=node.unit)
        elif ret == False:
            rq = node.client.write_registers(map['reg_pi_ori_nok'], 1, unit=node.unit)
        elif ret == 'ERROR':
            rq = node.client.write_registers(map['reg_pi_error'], 1, unit=node.unit)
        else:
            rq = node.client.write_registers(map['reg_pi_unknown_error'], 1, unit=node.unit)

    # Update the values of all the registers in the page
    # update_page()
