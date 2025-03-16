# tests/__init__.py

import pytest


# Example fixture: Dummy fixture to demonstrate valid fixture usage
@pytest.fixture
def sample_fixture():
    """Provide a sample data object for tests."""
    sample_data = {"key": "value"}
    return sample_data
