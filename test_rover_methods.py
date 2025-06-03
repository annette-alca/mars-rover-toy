import pytest
from rover import *
from unittest.mock import Mock, patch

@pytest.fixture
def robot1(): 
    """generic robot in the middle of the deck"""
    return Robot(2,1,'NORTH')

class TestRobotMethods:
    def test_Robot_instance_has_specified_attributes(self, robot1):
        assert isinstance(robot1,Robot)
        assert robot1.x == 2
        assert robot1.y == 1
        assert robot1.f == 'NORTH'
        assert robot1.report() == (2,1,'NORTH')

    def test_Robot_turn_method_updates_direction(self, robot1):
        robot1.turn('LEFT')
        assert robot1.f == 'WEST'
        robot1.turn('LEFT')
        assert robot1.f == 'SOUTH'
        robot1.turn('RIGHT')
        assert robot1.f == 'WEST'

    def test_Robot_move_method_updates_location(self,robot1):
        robot1.move()
        assert robot1.x, robot1.y == (2,2)
        robot1.move()
        assert robot1.x, robot1.y == (2,3)

    def test_Robot_move_does_not_exceed_constraints_and_moves_after_turning(self):
        robot2 = Robot(4,4,'NORTH')
        robot2.move
        assert robot2.x, robot2.y == (4,4) #no movement
        assert robot2.report() == (4,4,'NORTH') #no movement
        robot2.turn('LEFT')
        assert robot2.report() == (4,4,'WEST')
        robot2.move()
        assert robot2.report() == (3,4,'WEST') #movement allowed again

class TestInteractiveMain:        
    def test_PLACE_command_creates_Robot_instance_with_valid_values(self):
        #EXIT had to be added to end recursion and return robot object.
        input_mock = Mock(side_effect=['PLACE 3,1,EAST','EXIT'])
        with patch('rover.sys.stdin.readline', input_mock):
            robot = main()
            assert isinstance(robot,Robot)
            assert robot.x, robot.y == (3,1)
            assert robot.f == 'EAST'
            assert robot.report() == (3,1,'EAST')

    def test_PLACE_command_creates_no_Robot_with_invalid_values(self):
        input_mock = Mock(side_effect=['PLACE 22,77,88','EXIT'])
        with patch('rover.sys.stdin.readline', input_mock): #mock input values with specified side_effect
            robot = main()
            assert robot == None

    def test_of_various_series_of_commands_return_expected_report_values(self,capsys):
        #EXIT had to be added to end recursion and return robot object.
        input_outputs = [   # (text input as list of commands, expected report)
            (["PLACE 0,0,NORTH","MOVE","REPORT","EXIT"],(0,1,'NORTH')),
            (["PLACE 0,0,NORTH","LEFT","REPORT","EXIT"],(0,0,'WEST')),
            (["PLACE 1,2,EAST","MOVE","MOVE","LEFT","MOVE","REPORT","EXIT"],(3,3,'NORTH'))]
        for text,expected_report in input_outputs:
            input_mock = Mock(side_effect=text)
            with patch('rover.sys.stdin.readline', input_mock): #replace values in std_input with text
                robot = main()
                captured = capsys.readouterr() #capture std output
                assert robot.report() == expected_report
                assert f"Output: {expected_report}" in captured.out
                assert "Good-bye" in captured.out
            