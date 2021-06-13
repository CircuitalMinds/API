"""
Solvers define how a pde is solved, i.e., advanced in time.
.. autosummary::
.. codeauthor:: Alan Matzumiya <alan.matzumiya@gmail.com>
"""

from . import setup_solver

solver_fpk = setup_solver.SolverFPK
