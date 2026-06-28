import pytest
from docgen.entities import Font

@pytest.mark.parametrize("path, name", [("src/test/fixtures/font.glyphs", "TT Rationalist")])
def test_creating_font(path, name):
    font = Font(path)
    assert font.font_name == name
