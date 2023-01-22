def test_check_phrase(capsys):
    try:
        assert len(str(capsys)) < 15
    except AssertionError:
        print("Wrong phrase length")


phrase = input("Set a phrase: ")
test_check_phrase(phrase)