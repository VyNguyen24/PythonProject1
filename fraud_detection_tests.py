import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # example from spec
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    print("pass1")
    # add more test cases here


# write other test functions here
def test_extract_election_votes():
    assert len(fd.extract_election_votes("election-iran-2009.csv", ["\
        Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])) == 120
    assert len(fd.extract_election_votes("election-iran-2009.csv", ["\
        Ahmadinejad"])) == 30
    print("pass2")


def test_mean_squared_error():
    assert fd.mean_squared_error([1, 4, 9], [6, 5, 4]) == 17.0
    print("pass3")


def test_calculate_mse_with_uniform(histogram):
    assert math.isclose(fd.calculate_mse_with_uniform(histogram),
                        0.000739583333333)
    print("pass4")


def main():
    numbers = fd.extract_election_votes("election-iran-2009.csv", ["\
        Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    histogram = fd.ones_and_tens_digit_histogram(numbers)
    test_ones_and_tens_digit_histogram()
    test_extract_election_votes()
    test_mean_squared_error()
    test_calculate_mse_with_uniform(histogram)
    # call other test functions here


if __name__ == "__main__":
    main()
