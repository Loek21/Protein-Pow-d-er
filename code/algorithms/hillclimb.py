from .generalfunctions import stability_calculator, make_move

def pullmove(lattice):
    """Hill climb algorithm based on diagonal pull moves"""

    # get the chain
    chain = lattice.get_list()