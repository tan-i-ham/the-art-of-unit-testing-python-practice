from part1.log_analyzer import LogAnalyzer


class TestLogAnalyzer:

    def test_is_valid_log_filename_bad_extension_return_false(self):
        log_analyzer = LogAnalyzer()

        result = log_analyzer.is_valid_log_filename("filewithbadextension.foo")

        assert result is False

    def test_is_valid_log_filename_good_extension_return_true(self):
        log_analyzer = LogAnalyzer()

        result = log_analyzer.is_valid_log_filename("ZZZwdwd.SLF")

        assert result is True

    def test_is_valid_log_filename_lower_case_good_extension_return_true(self):
        log_analyzer = LogAnalyzer()

        result = log_analyzer.is_valid_log_filename("lowerNAME.slf")

        assert result is True
