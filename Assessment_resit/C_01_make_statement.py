# Functions go here
def make_statement(statement, decoration, amount=3):
    # Emphasise headings by adding decoration to the start and end.
    print(f"{decoration * amount} {statement} {decoration * amount}\n")

# Main routine goes here
make_statement("Instructions", "ℹ️")