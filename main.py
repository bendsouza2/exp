try:
    from test_key import fake_key, fake_id
    import other
except ModuleNotFoundError:
    pass


def multiply(x, y):

    ans = x * y
    return ans
