class MessageBuilder:

    @staticmethod
    def build(user: str, greeting_msg: str):
        return user + greeting_msg


class TestAvoidLogic:

    def test_production_logic_problem(self):
        user: str = "USER"
        greeting: str = "GREETING"
        actual: str = MessageBuilder.build(user, greeting)

        assert user + greeting == actual
