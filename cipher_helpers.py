def run_cipher_tests(ciphers_to_test, test_messages):
    """Encode, decode, and verify each cipher against the supplied messages."""

    for cipher in ciphers_to_test:
        print(f"\nCipher: {cipher}")
        print("=" * 50)
        for name, msg in test_messages.items():
            encoded_msg = cipher.encode(msg)
            decoded_msg = cipher.decode(encoded_msg)

            print(f"[{name}] Original: {msg}")
            print(f"[{name}] Encoded : {encoded_msg}")
            print(f"[{name}] Decoded : {decoded_msg}")
            print("-" * 50)

            assert msg == decoded_msg, f"Decoding failed for {name} using {cipher}!"
