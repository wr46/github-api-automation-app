class ContentLine:
    def __init__(self, line: str, start_idx: int, end_idx: int):
        self.line = line
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.indentation = len(line) - len(line.lstrip(' '))
