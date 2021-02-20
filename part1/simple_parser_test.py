from part1.simple_parser import SimpleParser


class SimpleParserTests:

    @staticmethod
    def test_return_zero_when_input_is_empty_string():
        try:
            parser = SimpleParser()
            result = parser.parse_and_sum("")
            if result != 0:
                print("@***SimpleParserTests.TestReturnsZeroWhenEmptyString:\n---"
                      "\nParse and sum should have returned 0 on an empty string")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        SimpleParserTests.test_return_zero_when_input_is_empty_string()
    except Exception as e:
        print(e)
