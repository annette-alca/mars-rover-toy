import pytest
from other_classes import *

class TestTableClass:
    def test_table_class_instance_has_specified_attributes(self):
        table = Table(4,10)
        assert isinstance(table,Table)
        assert table.bound_x == 4
        assert table.bound_y == 10
    
    def test_table_class_raises_OutOfBoundsError_for_out_of_bounds_coordinates(self):
        table = Table(5,5)
        with pytest.raises(OutOfBoundsError) as err:
            table.boundary_check((5,6))

class TestFacingClass:
    def test_facing_class_instance_has_specified_attributes(self):
        f = Facing('NORTH')
        assert isinstance(f,Facing)
        assert f.f == 'NORTH'
    
    def test_facing_class_raises_DirectionInvalidError_for_invalid_value(self):
        with pytest.raises(DirectionInvalidError) as err:
            f = Facing('invalid')