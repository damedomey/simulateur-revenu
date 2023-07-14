from utils.model import Address


class DataCorrespondence:
    """
    Represent the correspondence with the values in Excel file
    """
    # Client information
    client_name = Address("E9", writable=True)
    client_profession = Address("E11")

    profit_before_all_contribution = Address("H26", data_type="int", writable=True) # Bénéfice avant déduction des cotisations (et avant déduction de la rémunération pour l'EI à l'IS)
    optional_contribution = Address("H27", data_type="int", writable=True)

    executive_compensation = Address("H29", data_type="int", writable=True)
    gross_dividends_paid = Address("H30", data_type="int", writable=True)

    profit_before_contribution_ir = Address("H41", data_type="int")
    profit_before_contribution_is = Address("K41", data_type="int")
    contribution_ir = Address("H43", data_type="int")
    contribution_is = Address("K43", data_type="int")

    profit_ir = Address("H44", data_type="int")
    profit_is = Address("K44", data_type="int")





