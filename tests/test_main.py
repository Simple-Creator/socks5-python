"""Tests for the main module."""

from socks5.main import main


def test_main():
    """Test the main function."""
    assert main() == 0