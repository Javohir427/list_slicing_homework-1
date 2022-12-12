def main(numbers):
    """
    A list called numbers is given. Return the items in the odd position.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    a = numbers[::2]
    return a
print(main([1, 2, 3, 4, 5]))