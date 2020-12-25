class SimpleParser:

    def parse_and_sum(self, numbers: str):
        if len(numbers) == 0:
            return 0
        if ',' not in numbers:
            return int(numbers)
        else:
            raise Exception("I can only handle 0 or 1 numbers for now!")
        


