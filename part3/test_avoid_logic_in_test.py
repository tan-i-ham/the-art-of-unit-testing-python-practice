class MessageBuilder:

    @staticmethod
    def build(user: str, greeting_msg: str):
        return user + " " + greeting_msg


class TestAvoidLogic:

    def test_production_logic_problem(self):
        actual: str = MessageBuilder.build("USER", "GREETING")

        assert "USER GREETING" == actual
