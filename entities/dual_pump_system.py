from entities.opc_mapping import OPCMapping
from entities.pump import Pump
from entities.valve import Valve


class DualPumpSystem:
    def __init__(self):
        self.na2 = OPCMapping(Pump("NA2"), Valve("NA2_valve"))
        self.na4 = OPCMapping(Pump("NA4"), Valve("NA4_valve"))