import inspect

from part1.simple_parser import SimpleParser
from part1.test_util import TestUtil


class SimpleParserTests:

    @staticmethod
    def test_return_zero_when_input_is_empty_string():
        test_name = inspect.stack()[0][3]
        try:
            parser = SimpleParser()
            result = parser.parse_and_sum("")
            if result != 0:
                TestUtil.show_problem(test_name, "Parse and sum should have returned 0 on an empty string")
        except Exception as ex:
            TestUtil.show_problem(test_name, str(ex))


if __name__ == "__main__":
    try:
        SimpleParserTests.test_return_zero_when_input_is_empty_string()
    except Exception as e:
        print(e)
