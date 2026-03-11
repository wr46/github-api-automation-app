from github_automation.utils.content_handler.content_line import ContentLine


def test_content_line_class_ok():
    content_line = ContentLine("      Teste line!", 1, 18)
    assert 1 == content_line.start_idx
    assert len(content_line.line) + content_line.start_idx == content_line.end_idx
    assert 6 == content_line.indentation


def test_content_line_class_no_indent_ok():
    content_line = ContentLine("Teste line!", 1, 12)
    assert 1 == content_line.start_idx
    assert len(content_line.line) + content_line.start_idx == content_line.end_idx
    assert 0 == content_line.indentation


def test_content_line_class_alt_ok():
    content_line = ContentLine(" Teste line!", 2, 14)
    assert 2 == content_line.start_idx
    assert len(content_line.line) + content_line.start_idx == content_line.end_idx
    assert 1 == content_line.indentation


def test_content_line_class_empty_ok():
    content_line = ContentLine("", 2, 2)
    assert 2 == content_line.start_idx
    assert len(content_line.line) + content_line.start_idx == content_line.end_idx
    assert 0 == content_line.indentation
