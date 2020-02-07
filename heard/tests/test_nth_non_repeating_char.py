from heard.nth_non_repeating_char_in_a_string import nth_non_repeating_char


def test_first_non_repeating():
    res = nth_non_repeating_char(string="sivas")
    assert res == "i"


def test_second_non_repeating():
    res = nth_non_repeating_char(string="sivas", pos=2)
    assert res == "v"


def test_negative_all_repeating():
    res = nth_non_repeating_char(string="sivasiva", pos=2)
    assert res == None


def test_no_repeating():
    res = nth_non_repeating_char(string="siva")
    assert res == "s"
