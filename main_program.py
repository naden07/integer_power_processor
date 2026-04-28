from io_data_manager import FileHandler
from processor import DataProcessor

class IntegerApp:
    """Main Application Controller."""

    def __init__(self, source_file):
        self.source = source_file
        self.file_io = FileHandler()
        self.logic = DataProcessor()

    def run(self):
        print("--- Integer Power Processor Starting ---")

        #1. Read
        numbers = self.file_io.read_integers(self.source)

        if not numbers:
            return

        #2. Process
        evens_squared = self.logic.process_evens(numbers)
        odds_cubed = self.logic.process_odds(numbers)

        # 3. Write
        self.file_io.write_results("double.txt", evens_squared)
        self.file_io.write_results("triple.txt", odds_cubed)

        print("--- Processing Complete ---")


if __name__ == "_main_":
    app = IntegerApp("integers.txt")
    app.run()
