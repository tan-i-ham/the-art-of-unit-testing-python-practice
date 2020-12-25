class LogAnalyzer:
    def is_valid_log_filename(self, filename: str):
        if filename.lower().endswith(".slf"):
            return True
        return False

