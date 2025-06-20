import pytest
from rover import *
from other_classes import *
from unittest.mock import Mock, patch

@pytest.fixture
def robot1(): 
    """generic robot in the middle of the deck"""
    return Robot(2,1,'NORTH')

class TestRobotMethods:
    def test_Robot_instance_has_specified_attributes(self, robot1):
        assert isinstance(robot1,Robot)
        assert robot1.coordinates == (2,1)
        assert robot1.f == Facing('NORTH')
        assert robot1.report() == (2, 1, Facing('NORTH'))

    def test_Robot_turn_method_updates_direction(self, robot1):
        robot1.turn('LEFT')
        assert robot1.f == Facing('WEST')
        robot1.turn('LEFT')
        assert robot1.f == Facing('SOUTH')
        robot1.turn('RIGHT')
        assert robot1.f == Facing('WEST')

    def test_Robot_move_method_updates_location(self,robot1):
        robot1.move()
        assert robot1.coordinates == (2,2)
        robot1.move()
        assert robot1.coordinates == (2,3)

    def test_Robot_move_does_not_exceed_table_constraints(self):
        robot2 = Robot(4,4,'NORTH')
        robot2.move
        assert robot2.coordinates == (4,4) #no movement
        assert robot2.report() == (4, 4, Facing('NORTH')) #no movement

    def test_Robot_able_to_move_again_after_hitting_boundary_and_turning(self):
        robot2 = Robot(4,4,'NORTH')
        robot2.move
        assert robot2.report() == (4, 4, Facing('NORTH')) #no movement
        robot2.turn('LEFT')
        assert robot2.report() == (4, 4, Facing('WEST'))
        robot2.move()
        assert robot2.report() == (3, 4, Facing('WEST')) #movement allowed again

class TestInteractiveMain:        
    def test_PLACE_command_creates_Robot_instance_with_valid_values(self):
        #EXIT had to be added to end recursion and return robot object.
        input_mock = Mock(side_effect=['PLACE 3,1,EAST','EXIT'])
        with patch('rover.sys.stdin.readline', input_mock):
            robot = main()
            assert isinstance(robot,Robot)
            assert robot.coordinates == (3,1)
            assert robot.f == Facing('EAST')
            assert robot.report() == (3, 1, Facing('EAST'))

    def test_PLACE_command_creates_no_Robot_with_invalid_values(self):
        input_mock = Mock(side_effect=['PLACE 22,77,88','EXIT'])
        with patch('rover.sys.stdin.readline', input_mock): #mock input values with specified side_effect
            robot = main()
            assert robot == None

class TestMainandRobotWithTestData:

    def test_data1(self,capsys):
        #EXIT had to be added to end recursion and return robot object.
        input_text = ["PLACE 0,0,NORTH","LEFT","REPORT","EXIT"]
        expected_report = "(0, 0, WEST)"
        input_mock = Mock(side_effect=input_text)
        with patch('rover.sys.stdin.readline', input_mock): #replace values in std_input with text
            robot = main()
            captured = capsys.readouterr() #capture std output
            assert str(robot.report()) == expected_report
            assert f"Output: {expected_report}" in captured.out

    def test_data2(self,capsys):
        input_text = ["PLACE 0,0,NORTH","MOVE","REPORT","EXIT"]
        expected_report = "(0, 1, NORTH)"
        input_mock = Mock(side_effect=input_text)
        with patch('rover.sys.stdin.readline', input_mock):
            robot = main()
            captured = capsys.readouterr()
            assert str(robot.report()) == expected_report
            assert f"Output: {expected_report}" in captured.out

    def test_data3(self,capsys):
        input_text = ["PLACE 1,2,EAST","MOVE","MOVE","LEFT","MOVE","REPORT","EXIT"]
        expected_report = "(3, 3, NORTH)"
        input_mock = Mock(side_effect=input_text)
        with patch('rover.sys.stdin.readline', input_mock):
            robot = main()
            captured = capsys.readouterr() 
            assert str(robot.report()) == expected_report
            assert f"Output: {expected_report}" in captured.out
