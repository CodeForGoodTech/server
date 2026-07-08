import pytest

from utils.markdown_handler import extract_description_from_body


def test_extract_description_from_body_returns_description_section():
    body = """### Ticket Contents

## Description
Provide a brief project description, outlining the need and measurable goals of the feature to be developed.

### Goals

## Goals
- [ ] [Goal 1]
"""

    assert extract_description_from_body(body) == "Provide a brief project description, outlining the need and measurable goals of the feature to be developed."


def test_extract_description_from_body_falls_back_to_body_when_no_description_heading():
    body = "This is the full body text"
    assert extract_description_from_body(body) == "This is the full body text"
