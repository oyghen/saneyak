import saneyak


def main():
    actual = saneyak.__name__
    expected = "saneyak"
    if actual == expected:
        print("smoke test passed")
    else:
        raise RuntimeError("smoke test failed")


if __name__ == "__main__":
    main()
