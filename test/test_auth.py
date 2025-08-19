def test_token_generation():
    from app.auth import generate_token, verify_token
    token = generate_token(1, 'admin')
    decoded = verify_token(token)
    assert decoded['role'] == 'admin'

