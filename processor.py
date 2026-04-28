class DataProcessor:
    """Handles the logic of filtering and transforming integers."""

    def process_evens(self, numbers):
        #even integers: n^2
        return [n ** 2 for n in numbers if n % 2 == 0]

    def process_odds(self, numbers):
        #odd integers: n^3
        return [n ** 3 for n in numbers if n % 2 != 0]