from typing import List

from github.ContentFile import ContentFile

from github_automation.utils.content_handler.content_line import ContentLine
from github_automation.utils.content_handler.indentation_config import IndentationConfig


class ContentHandler:
    def __init__(self, content_file: ContentFile, indentation: IndentationConfig = None):
        self._content_file = content_file
        self.indentation = IndentationConfig() if indentation is None else indentation
        self._new_content: bytes = content_file.decoded_content

    def _content_update(self, content: str):
        self._new_content = bytes(content, 'utf-8')

    @property
    def content(self) -> bytes:
        return self._new_content

    @property
    def content_sha(self) -> str:
        return self._content_file.sha

    @property
    def content_path(self) -> str:
        return self._content_file.path

    @property
    def content_decoded(self) -> str:
        return self._new_content.decode('utf-8')

    @property
    def has_content_update(self) -> bool:
        return self._new_content != self._content_file.decoded_content

    def get_lines(self, search: str, from_index: int = 0, lines: List[ContentLine] = None) -> List[ContentLine]:
        """ Return a list of ContentLine where sub parameter is found in given content. """
        if len(search) == 0:
            return []

        lines = [] if lines is None else lines
        content = self.content_decoded
        index_at = content.find(search, from_index)
        if index_at == -1:
            return lines

        start_idx = content.rfind('\n', from_index, index_at) + 1
        end_idx = content.find('\n', index_at)
        lines.append(ContentLine(content[start_idx:end_idx], start_idx, end_idx))

        return self.get_lines(search, end_idx, lines)

    def insert_line_by_content(self, line: str, content_lines: List[ContentLine], indentation: int = -1, before: bool = False):
        """
        Return the result of insert line into content with default same indentation and default after the given ContentLine.
        """
        content = self.content_decoded
        content_lines.sort(key=lambda l: l.start_idx, reverse=True)
        for content_line in content_lines:
            indent = indentation if indentation > -1 else content_line.indentation
            index_insert = content_line.start_idx if before is True else content_line.end_idx + 1
            content = content[:index_insert] + self.indentation.indent(line, indent) + content[index_insert:]

        self._content_update(content)

    def insert_line_by_str(self, line: str, search: str, indentation: int = -1, before: bool = False):
        self.insert_line_by_content(line, self.get_lines(search), indentation, before)
