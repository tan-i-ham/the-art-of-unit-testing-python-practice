from pytest import raises

from part1.simple_parser import SimpleParser


class TestSimpleParser:

    def test_return_zero_when_input_is_empty_string(self):
        parser = SimpleParser()

        actual = parser.parse_and_sum("")

        assert 0 == actual

    def test_has_non_number_str(self):
        parser = SimpleParser()

        with raises(Exception) as e:
            parser.parse_and_sum(",124")

        assert "I can only handle 0 or 1 numbers for now!" in str(e.value)
