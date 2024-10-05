from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
from pytest import approx
import pytest

#Test function to check the correct water column
def test_water_column_height():
    expected_water_column = [
    [0,0,0],
    [0,10,7.5],
    [25,0,25],
    [48.3,12.8,57.9]
    ]
    count_exp_water_column = len(expected_water_column)
    i = 0
    while i < count_exp_water_column:
        assert water_column_height(expected_water_column[i][0], expected_water_column[i][1]) == approx(expected_water_column[i][2])
        i += 1
#Test function to check the correct pressure gain from a specific water height
def test_pressure_gain_from_water_height():
    expected_pressure = [
    [0, 0, 0.001],
    [30.2, 295.628, 0.001],
    [50, 489.45, 0.001]
    ]
    count_exp_pressure = len(expected_pressure)
    i = 0
    while i < count_exp_pressure:
        assert pressure_gain_from_water_height(expected_pressure[i][0]) == approx(expected_pressure[i][1], abs=expected_pressure[i][2])
        i += 1
#Test function to check the correct pressure loss from a pipe
def test_pressure_loss_from_pipe():
    expected_pressure_loss = [
    [0.048692, 0, 0.018, 1.75, 0, 0.001],
    [0.048692, 200, 0, 1.75, 0, 0.001],
    [0.048692, 200, 0.018, 0, 0, 0.001],
    [0.048692, 200, 0.018, 1.75, -113.008, 0.001],
    [0.048692, 200, 0.018, 1.65, -100.462, 0.001],
    [0.28687, 1000, 0.013, 1.65, -61.576, 0.001],
    [0.28687, 1800.75, 0.013, 1.65, -110.884, 0.001]
    ]
    count_exp_pressure_loss = len(expected_pressure_loss)
    i = 0
    while i < count_exp_pressure_loss:
        assert pressure_loss_from_pipe(expected_pressure_loss[i][0],expected_pressure_loss[i][1],expected_pressure_loss[i][2],expected_pressure_loss[i][3]) == approx(expected_pressure_loss[i][4], abs=expected_pressure_loss[i][5])
        i += 1
#Test function to check the correct pressure loss from fittings
def test_test_pressure_loss_from_fittings():
    expected_pressure_loss = [
    [0, 3, 0, 0.001],
    [1.65, 0, 0, 0.001],
    [1.65, 2, -0.109, 0.001],
    [1.75, 2, -0.122, 0.001],
    [1.75, 5, -0.306, 0.001]
    ]
    count_expected_pressure_loss = len(expected_pressure_loss)
    i = 0
    while i < count_expected_pressure_loss:
        assert pressure_loss_from_fittings(expected_pressure_loss[i][0], expected_pressure_loss[i][1]) == approx(expected_pressure_loss[i][2], abs=expected_pressure_loss[i][3])
        i += 1
#Test function to check the correct Reynollds number
def test_reynolds_number():
    expected_reynolds_number = [
    [0.048692, 0, 0, 1],
    [0.048692, 1.65, 80069, 1],
    [0.048692, 1.75, 84922, 1],
    [0.28687, 1.65, 471729, 1],
    [0.28687, 1.75, 500318, 1]
    ]
    count_expected_reynolds_number = len(expected_reynolds_number)
    i = 0
    while i < count_expected_reynolds_number:
        assert reynolds_number(expected_reynolds_number[i][0], expected_reynolds_number[i][1]) == approx(expected_reynolds_number[i][2], abs=expected_reynolds_number[i][3])
        i += 1
#Test function to check the correct pressure loss from pipe reduction
def test_pressure_loss_from_pipe_reduction():
    expected_pressure_loss = [
    [0.28687, 0, 1, 0.048692, 0, 0.001],
    [0.28687, 1.65, 471729, 0.048692, -163.744, 0.001],
    [0.28687, 1.75, 500318, 0.048692, -184.182, 0.001]
    ]
    count_exp_pressure_loss = len(expected_pressure_loss)
    i = 0
    while i < count_exp_pressure_loss:
        assert pressure_loss_from_pipe_reduction(expected_pressure_loss[i][0],expected_pressure_loss[i][1],expected_pressure_loss[i][2],expected_pressure_loss[i][3]) == approx(expected_pressure_loss[i][4], abs=expected_pressure_loss[i][5])
        i += 1



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])