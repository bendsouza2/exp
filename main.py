try:
    from test_key import fake_key, fake_id
    import other
except ModuleNotFoundError:
    pass

print(fake_id, fake_key)