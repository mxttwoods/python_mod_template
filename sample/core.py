"""
The core module is the main module of the project.
"""

from . import helpers


def get_hmm():
    """Get a thought."""
    return "hmmm..."


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
