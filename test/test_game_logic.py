from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_check_guess_hints_are_not_swapped():
    high_outcome, high_message = check_guess(60, 50)
    low_outcome, low_message = check_guess(40, 50)

    assert high_outcome == "Too High"
    assert "LOWER" in high_message
    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message


def test_check_guess_handles_numeric_string_secret():
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_still_parses_numeric_input():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


def test_update_score_first_win_not_off_by_one_attempt():
    # In app flow, attempts are incremented before scoring.
    # Winning on the first actual guess passes attempt_number=2.
    score = update_score(current_score=0, outcome="Win", attempt_number=2)
    assert score == 90


def test_hard_range_is_harder_than_normal():
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert normal_low == 1
    assert hard_low == 1
    assert hard_high > normal_high
