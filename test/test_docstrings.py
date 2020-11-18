from docstrings import _add_docstring
import algorithm


def test_docstring_added():
    def function_without_docstring():
        return None

    function_with_docstring = _add_docstring(
        function_without_docstring, 'a docstring')

    assert function_with_docstring.__doc__ == 'a docstring'


def test_calculate_weighted_score_and_attempts_has_docstring():
    assert algorithm.calculate_weighted_score_and_attempts.__doc__ is not None
