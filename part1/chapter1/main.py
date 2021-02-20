from part1.chapter1.simple_parser_test import SimpleParserTests

if __name__ == "__main__":
    try:
        SimpleParserTests.test_return_zero_when_input_is_empty_string()
    except Exception as e:
        print(e)
