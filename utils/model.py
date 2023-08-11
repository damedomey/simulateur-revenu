class Address:
    """
        Represent a address of a cell in Excel file
    """

    def __init__(self, cell, data_type="str", sheet="simulateur", writable=False):
        self.sheet = sheet
        self.cell = cell
        self.data_type = data_type
        """This is used to reduce the risk of error"""
        self.writable = writable


class SimulationResult:
    def __init__(self):
        self.client = _Client()
        self.profit_before_all = 0
        self.IR = _Profit()
        self.IS = _Profit()

    def set_client_name(self, name):
        self.client.name = name

    def set_profit_before_all_contribution(self, profit):
        self.profit_before_all = profit

    def set_ir_profit_before_contribution(self, profit):
        self.IR.before_contribution = profit

    def set_is_profit_before_contribution(self, profit):
        self.IR.before_contribution = profit

    def set_ir_contribution(self, contribution):
        self.IR.contribution = contribution

    def set_is_contribution(self, contribution):
        self.IS.contribution = contribution

    def set_is_profit_value(self, profit):
        self.IS.value = profit

    def set_ir_profit_value(self, profit):
        self.IR.value = profit

class _Client:
    def __init__(self):
        self.name = ""


class _Profit:
    def __init__(self):
        self.before_contribution = 0
        self.contribution = 0
        self.value = 0 # Bénéfice (avant IS pour l'EI à l'IS)
