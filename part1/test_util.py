class TestUtil:
    @staticmethod
    def show_problem(test: str, message: str):
        msg = "---{0}---{1} --------------------".format(test, message)
        print(msg)
