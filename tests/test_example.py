from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_reverse_for_palindrome():
    assert reverse('шалаш') == 'шалаш'


def test_reverse_with_spaces():
    assert reverse('hello world') == 'dlrow olleh'


def test_reverse_with_numbers():
    assert reverse('123') == '321'
