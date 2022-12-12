def main(list1,n):
    """
    A list of several elements is given. Return all items except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    a = list1[n:]
    return a
print(main(['a', 'b', 'c', 'd', 'e', 'f'],3)) 