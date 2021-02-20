from part3.log_analyzer import LogAnalyzer


class TestLogAnalyzer:

    def test_semantics_change(self):
        logan = make_default_analyzer()

        assert logan.is_valid("abc") is False


def make_default_analyzer():
    logan = LogAnalyzer()
    logan.initialize()
    return logan
