import pytest
from solution import generate_pyramid


class TestGeneratePyramid:
    """Test suite for the generate_pyramid function."""
    
    def test_pyramid_with_default_character(self):
        """Test pyramid generation with default '*' character."""
        result = generate_pyramid(3)
        expected = "  *  \n *** \n*****\n"
        assert result == expected
    
    def test_pyramid_with_custom_character(self):
        """Test pyramid generation with custom characters."""
        result = generate_pyramid(3, '#')
        expected = "  #  \n ### \n#####\n"
        assert result == expected
    
    def test_pyramid_single_level(self):
        """Test edge case: pyramid with only 1 level."""
        result = generate_pyramid(1)
        expected = "*\n"
        assert result == expected
    
    def test_pyramid_single_level_custom_char(self):
        """Test edge case: single level with custom character."""
        result = generate_pyramid(1, '+')
        expected = "+\n"
        assert result == expected
    
    def test_pyramid_max_levels(self):
        """Test boundary case: pyramid with maximum 20 levels."""
        result = generate_pyramid(20)
        lines = result.strip().split('\n')
        # Should have 20 lines
        assert len(lines) == 20
        # First line should have 1 character
        assert '*' in lines[0] and len(lines[0].strip()) == 1
        # Last line should have 39 characters (2*20-1)
        assert len(lines[-1].strip()) == 39
    
    def test_pyramid_structure_5_levels(self):
        """Test the structure of a 5-level pyramid."""
        result = generate_pyramid(5)
        lines = result.strip().split('\n')
        
        # Should have 5 lines
        assert len(lines) == 5
        
        # Check each line has correct number of characters
        for i, line in enumerate(lines):
            level = i + 1
            expected_chars = 2 * level - 1
            assert len(line.strip()) == expected_chars
    
    def test_pyramid_different_characters(self):
        """Test pyramid with various characters."""
        characters = ['+', '-', '=', '|', '@']
        for char in characters:
            result = generate_pyramid(3, char)
            # Check that the character is used correctly
            assert char in result
            # Check structure
            lines = result.strip().split('\n')
            assert len(lines) == 3
            assert len(lines[0].strip()) == 1
            assert len(lines[1].strip()) == 3
            assert len(lines[2].strip()) == 5
    
    def test_pyramid_ends_with_newline(self):
        """Test that pyramid ends with a newline character."""
        result = generate_pyramid(3)
        assert result.endswith('\n')
    
    def test_newline_between_levels(self):
        """Test that each level is separated by a newline."""
        result = generate_pyramid(3)
        lines = result.split('\n')
        # Should have 4 elements: 3 levels + empty string at end
        assert len(lines) == 4
        assert lines[-1] == ''  # Last element should be empty due to trailing newline
    
    # Error handling tests
    def test_n_below_minimum(self):
        """Test that ValueError is raised when n < 1."""
        with pytest.raises(ValueError, match="n must be an integer between 1 and 20"):
            generate_pyramid(0)
    
    def test_n_above_maximum(self):
        """Test that ValueError is raised when n > 20."""
        with pytest.raises(ValueError, match="n must be an integer between 1 and 20"):
            generate_pyramid(21)
    
    def test_n_negative(self):
        """Test that ValueError is raised with negative n."""
        with pytest.raises(ValueError, match="n must be an integer between 1 and 20"):
            generate_pyramid(-5)
    
    def test_n_not_integer(self):
        """Test that ValueError is raised when n is not an integer."""
        with pytest.raises(ValueError, match="n must be an integer between 1 and 20"):
            generate_pyramid(5.5)
    
    def test_char_not_string(self):
        """Test that ValueError is raised when char is not a string."""
        with pytest.raises(ValueError, match="char must be a single character string"):
            generate_pyramid(5, 42)
    
    def test_char_empty_string(self):
        """Test that ValueError is raised with empty char string."""
        with pytest.raises(ValueError, match="char must be a single character string"):
            generate_pyramid(5, '')
    
    def test_char_multiple_characters(self):
        """Test that ValueError is raised when char has multiple characters."""
        with pytest.raises(ValueError, match="char must be a single character string"):
            generate_pyramid(5, 'ab')
    
    def test_pyramid_centered_properly(self):
        """Test that pyramid levels are centered correctly."""
        result = generate_pyramid(3)
        lines = result.split('\n')[:-1]  # Exclude empty string from trailing newline
        
        for i, line in enumerate(lines):
            # Each line should be centered within the max width
            stripped = line.strip()
            # Check that centering leaves roughly equal padding on both sides
            left_padding = len(line) - len(line.lstrip())
            right_padding = len(line) - len(line.rstrip())
            # The difference should be at most 1 character due to odd/even centering
            assert abs(left_padding - right_padding) <= 1
