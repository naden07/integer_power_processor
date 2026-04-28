import os

class FileHandler:
    """Handles all file reading and writing operations."""

    @staticmethod
    def read_integers(filename):
        if not os.path.exists(filename):
            print(f"Error: {filename} not found.")
            return []
        with open(filename, 'r') as file:
            # Reads lines, strips whitespace, and converts to int
            return [int(line.strip()) for line in file if line.strip()]

    @staticmethod
    def write_results(filename, data):
        with open(filename, 'w') as file:
            for item in data:
                file.write(f"{item}\n")
        print(f"Successfully created: {filename}")