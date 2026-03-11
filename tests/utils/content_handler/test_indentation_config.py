import pytest

from github_automation.utils.content_handler.indentation_config import IndentationConfig


def test_indentation_config_class_default_ok():
    block = "This is a line!"
    indentation = 0
    config = IndentationConfig()
    assert 0 == config.shift
    assert block == config.indent(block, indentation)


def test_indentation_config_class_indent_ok():
    block = "This is a line!"
    indentation = 4
    config = IndentationConfig()
    assert 0 == config.shift
    assert ' ' * indentation + block == config.indent(block, indentation)


def test_indentation_config_class_negative_shift_ok():
    block = "This is a line!"
    indentation = 4
    shift = -2
    config = IndentationConfig(shift)
    assert shift == config.shift
    assert ' ' * 2 + block == config.indent(block, indentation)


def test_indentation_config_class_positive_shift_ok():
    block = "This is a line!"
    indentation = 4
    shift = 2
    config = IndentationConfig(shift)
    assert shift == config.shift
    assert ' ' * 6 + block == config.indent(block, indentation)


def test_indentation_config_class_block_ok():
    block = "This is a line!\nThis is a 2nd line!\n"
    indent_block = "    This is a line!\n    This is a 2nd line!\n"
    indentation = 4
    config = IndentationConfig()
    assert indent_block == config.indent(block, indentation)


def test_indentation_config_class_block_alt_ok():
    block = "This is a line!\nThis is a 2nd line!"
    indent_block = "    This is a line!\n    This is a 2nd line!"
    indentation = 4
    config = IndentationConfig()
    assert indent_block == config.indent(block, indentation)


def test_indentation_config_class_empty_block_fail():
    block = "  "
    indentation = 4
    config = IndentationConfig()
    with pytest.raises(AssertionError):
        config.indent(block, indentation)


def test_indentation_config_class_negative_indentation_fail():
    block = "This is a line!\nThis is a 2nd line!"
    indentation = -1
    config = IndentationConfig()
    with pytest.raises(AssertionError):
        config.indent(block, indentation)
