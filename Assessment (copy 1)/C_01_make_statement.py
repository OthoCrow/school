# Functions go here
def make_statement(statement, decoration):
    # Emphasises headings by adding decorationg to the start and end

    print(f"{decoration * 3} {statement} {decoration * 3}\n")

# Main routine goes here
make_statement("Instructions", "ℹ️")