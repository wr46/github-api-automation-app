class IndentationConfig:
    def __init__(self, shift: int = 0):
        self.shift = shift

    def indent(self, block: str, indentation: int) -> str:
        """
        :param block: string
        :param indentation: integer
        :rtype: :string:`indented block`
        """
        assert block.strip(), "block can not be empty!"
        assert indentation >= 0, "indentation can not be negative"
        new_line = '\n'
        spaces = indentation if indentation + self.shift < 0 else indentation + self.shift
        if block.find(new_line) < 0:
            return ' ' * spaces + block

        lines = block.split(new_line)
        for idx, line in enumerate(lines):
            lines[idx] = line if 0 == len(line) else ' ' * spaces + line

        return new_line.join(lines)
