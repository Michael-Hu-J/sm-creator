import pytest
import time
from creator.core.android.GetDriver import baas_driver


@pytest.fixture(scope="class", name="driver")
def init_driver():
    driver = baas_driver()
    return driver

