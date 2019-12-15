import pytest
import statistics_generator

gold_values = [2, 3, 5, 10]
silver_values = [3, 4, 3, 2]
bronze_values = [4, 6, 2, 3]

@pytest.fixture
def supply_gold_silver_bronze_values():
    gold_values = [2, 3, 5, 10]
    silver_values = [3, 4, 3, 2]
    bronze_values = [4, 6, 2, 3]
    return [gold_values,silver_values,bronze_values]


def test_file1_average_values_for_all_medals_positive():
    list_of_averages_for_all_medals = statistics_generator.average_values(gold_values, silver_values, bronze_values)
    assert list_of_averages_for_all_medals['Gold'] == 5.0
    assert list_of_averages_for_all_medals['Silver'] == 3.0
    assert list_of_averages_for_all_medals['Bronze'] == 3.75


def test_max_value():
    max_min_values = statistics_generator.max_min_value(gold_values, silver_values, bronze_values)
    assert max_min_values[0]['Gold'] == 10
    assert max_min_values[0]['Silver'] == 4
    assert max_min_values[0]['Bronze'] == 6


def test_min_value():
    max_min_values = statistics_generator.max_min_value(gold_values, silver_values, bronze_values)
    assert max_min_values[1]['Gold'] == 2
    assert max_min_values[1]['Silver'] == 2
    assert max_min_values[1]['Bronze'] == 2

def test_variance():
    variance_std_deviation_values = statistics_generator.variance_std_deviation(gold_values, silver_values,
                                                                                bronze_values)
    assert variance_std_deviation_values[0]['Gold'] == 9.5
    assert variance_std_deviation_values[0]['Silver'] == 0.5
    assert variance_std_deviation_values[0]['Bronze'] == 2.1875


def test_std_deviaition():
    variance_std_deviation_values = statistics_generator.variance_std_deviation(gold_values, silver_values,
                                                                                bronze_values)
    assert f"{variance_std_deviation_values[1]['Gold']:.2f}" == '3.08'
    assert f"{variance_std_deviation_values[1]['Silver']:.2f}" == '0.71'
    assert f"{variance_std_deviation_values[1]['Bronze']:.2f}" == '1.48'


def test_correlation():
    correlation_values = statistics_generator.correlation(gold_values, silver_values)
    assert f"{correlation_values:.2f}" == '-0.80'


def test_mean():
    mean_gold = statistics_generator.mean(gold_values)
    mean_silver = statistics_generator.mean(silver_values)
    mean_bronze = statistics_generator.mean(bronze_values)
    assert mean_gold == 5.0
    assert mean_silver == 3.0
    assert mean_bronze == 3.75


# test_variance_positive()
# test_std_deviaition()
# test_mean()
# test_min_value()
# test_min_value()
# test_correlation()
