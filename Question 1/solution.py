def generate_pyramid(n, char='*'):
    """
    Generate a pyramid pattern of n levels using the specified character.
    
    Args:
        n: The number of levels in the pyramid (must be between 1 and 20)
        char: The character to use for constructing the pyramid (default '*', must be a single character)
    
    Returns:
        A string representing the pyramid pattern with each level centered
    
    Raises:
        ValueError: If n is not between 1 and 20, or if char is not a single character
    """
    # Validate n parameter
    if not isinstance(n, int) or n < 1 or n > 20:
        raise ValueError("n must be an integer between 1 and 20")
    
    # Validate char parameter
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("char must be a single character string")
    
    result = []
    max_width = 2 * n - 1
    
    for level in range(1, n + 1):
        # Number of characters in this level
        num_chars = 2 * level - 1
        # Create the line with the characters
        line = char * num_chars
        # Center the line
        centered_line = line.center(max_width)
        result.append(centered_line)
    
    return "\n".join(result) + "\n"

# Example usage
if __name__ == "__main__":
    print(generate_pyramid(3, '#'))