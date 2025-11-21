import saneyak


def main():
    result = saneyak.__name__
    expected = "saneyak"
    if result == expected:
        print("smoke test passed")
    else:
        raise RuntimeError("smoke test failed")


if __name__ == "__main__":
    main()
