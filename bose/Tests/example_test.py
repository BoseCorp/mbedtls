import pytest

from WearableTestUtils.DutUtils.dut_factory import DutFactory as Dut
from WearableTestUtils.DutUtils.bmap import Debug
from WearableTestUtils.DutUtils.products import Product
from WearableTestUtils.DutUtils.command.commands import BmapCommand

def test_debug_battery_get():
    dut = Dut.get_dut("LIZZO", product=Product.LIZZO)
    command = BmapCommand(Debug.Battery.Get)
    response = dut.execute(command)
    print(response)
    assert response != ""
