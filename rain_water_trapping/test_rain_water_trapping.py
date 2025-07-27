from rain_water_trapping.rain_water_trapping import TrappingRainWaterSolution


def test_trapping_rain_water1():
    input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = TrappingRainWaterSolution().trap(input)
    assert res == 6


def test_trapping_rain_water2():
    input = [4, 2, 0, 3, 2, 5]
    res = TrappingRainWaterSolution().trap(input)
    assert res == 9
