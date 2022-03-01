import pytest
import pathlib

if __name__ == "__main__":
    pytest.main(["-x", pathlib.Path(__file__).parent.resolve()])