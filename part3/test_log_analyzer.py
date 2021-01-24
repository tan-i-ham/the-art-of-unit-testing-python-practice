from part3.log_analyzer import LogAnalyzer


class TestLogAnalyzer:

    def test_semantics_change(self):
        logan = LogAnalyzer()
        logan.initialize()

        assert logan.is_valid("abc") is False
