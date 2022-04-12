import sys

import pytest
from pydantic import BaseModel

from dff_generic_response.dff_generic_response import GenericResponse, Link

# uncomment the following line, if you want to run your examples during the test suite or import from them
# sys.path.insert(0, "../")


def test_main():
    assert issubclass(GenericResponse, BaseModel)
    assert issubclass(Link, BaseModel)
