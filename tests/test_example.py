from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_to_empty_string():
    assert reverse('') == ''
