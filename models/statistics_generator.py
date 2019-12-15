import csv
from math import sqrt


def average_values(gold_medal_values, silver_medal_values, bronze_medal_values):
    """Retrieve the data for a given column for all medal winners

           Parameters:
           gold_medal_values (list of floats):
           silver_medal_values (list of floats):
           bronze_medal_values (list of floats):

           Returns:
           float:Gold medal values
           float:Silver medal values
           float:Bronze medal value

          """
    print(gold_medal_values, silver_medal_values, bronze_medal_values)
    list_of_averages_for_all_medals = {"Gold": sum(gold_medal_values) / len(gold_medal_values),
                                       "Silver": sum(silver_medal_values) / len(silver_medal_values),
                                       "Bronze": sum(bronze_medal_values) / len(bronze_medal_values)}
    print(list_of_averages_for_all_medals)
    return list_of_averages_for_all_medals


def mean(medal_values):
    """Takes in a list of floats and return a mean value

               Parameters:
               medal_values (list of floats):

               Returns:
               float: mean value
              """
    try:
        return sum(medal_values) / len(medal_values)

        # ZeroDivisionError - if the list is empty
        # TypeError - is the list is not all
    except (ZeroDivisionError, TypeError):
        return None


def max_min_value(gold_medal_values, silver_medal_values, bronze_medal_values):
    """Takes in 3 lists of floats for each medal value and returns the max and min age for each medal value

                   Parameters:
                   gold_medal_values (list of floats):
                    silver_medal_values (list of floats):
                    bronze_medal_values (list of floats):

                   Returns:
                   list of floats: max_value_for_all_medals
                   list of floats: min_value_for_all_medals
                  """

    max_value_for_all_medals = {"Gold": max(gold_medal_values), "Silver": max(silver_medal_values),
                                "Bronze": max(bronze_medal_values)}
    min_value_for_all_medals = {"Gold": min(gold_medal_values), "Silver": min(silver_medal_values),
                                "Bronze": min(bronze_medal_values)}

    return max_value_for_all_medals , min_value_for_all_medals


def variance_std_deviation(gold_medal_values, silver_medal_values, bronze_medal_values):
    """Takes in 3 lists of floats for each medal value and returns the variance and standard deviation
        for each medal value

               Parameters:
                            gold_medal_values (list of floats):
                            silver_medal_values (list of floats):
                            bronze_medal_values (list of floats):

               Returns:
                       list of floats: variance_for_all_medals
                       list of floats: std_deviation_for_all_medals
                      """

    variance_for_all_medals = {}
    average_values_for_medals = average_values(gold_medal_values, silver_medal_values, bronze_medal_values)
    variance_for_all_medals["Gold"] = sum((xi - average_values_for_medals['Gold']) ** 2 for xi in gold_medal_values) / len(gold_medal_values)
    variance_for_all_medals["Silver"] = sum((xi - average_values_for_medals['Silver']) ** 2 for xi in silver_medal_values) / len(silver_medal_values)
    variance_for_all_medals["Bronze"] = sum((xi - average_values_for_medals['Bronze']) ** 2 for xi in bronze_medal_values) / len(bronze_medal_values)
    std_deviation_for_all_medals = std_deviation(variance_for_all_medals)
    return variance_for_all_medals, std_deviation_for_all_medals


def std_deviation(variance_for_all_medals):
    """Takes in a lists of dictionaries containg the variances for each medal value. Return a dictionary of standard
        deviation values for each meadl value

                   Parameters:
                                gold_medal_values (list of floats):
                                silver_medal_values (list of floats):
                                bronze_medal_values (list of floats):

                   Returns:
                           list of floats: variance_for_all_medals
                           list of floats: std_deviation_for_all_medals
                          """
    std_deviation_for_all_medals = {"Gold": sqrt(variance_for_all_medals["Gold"]),
                                    "Silver": sqrt(variance_for_all_medals["Silver"]),
                                    "Bronze": sqrt(variance_for_all_medals["Bronze"])}
    return std_deviation_for_all_medals


def csv_medal_data_parser(column_key):
    """Retrieve the data for a given column for all medal winners

        Parameters:
        argument1 (int): column number to parse

        Returns:
        float:Gold medal values
        float:Silver medal values
        float:Bronze medal value

       """
    try:
        gold_medal_data = []
        silver_medal_data = []
        bronze_medal_data = []
        with open('athlete_events.csv', newline="", encoding="utf8") as datafile:
            datafile.readline()
            csvdatafile = csv.reader(datafile)
            for line in csvdatafile:
                if line[14] == "Gold" and line[column_key] != "NA":
                    gold_medal_data.append(float(line[column_key]))
                elif line[14] == "Silver" and line[column_key] != "NA":
                    silver_medal_data.append(float(line[column_key]))
                elif line[14] == "Bronze" and line[column_key] != "NA":
                    bronze_medal_data.append(float(line[column_key]))

        return gold_medal_data, silver_medal_data, bronze_medal_data
    except FileNotFoundError as fnf_error:
        print("no file found")
    except IsADirectoryError as dir_error:
        print("no file found")


def correlation(x_vals, y_vals):
    """
    Calculate the correlation of two lists

    Parameters
    x_vals : list
        A list of values.
    y_vals : list
    Returns
    float: The correlation between the lists, or None if it cannot be calculated.
    """

    # get mean values
    x_mean = mean(x_vals)
    y_mean = mean(y_vals)

    # create a list of the deviations
    x_deviations = [x - x_mean for x in x_vals]
    y_deviations = [y - y_mean for y in y_vals]

    # Create a list of the deviations multiplied
    xy_deviations = [x * y for (x, y) in zip(x_deviations, y_deviations)]

    # Create a list of the deviations squared
    x_sqd_deviations = [(x - x_mean) ** 2 for x in x_vals]
    y_sqd_deviations = [(y - y_mean) ** 2 for y in y_vals]

    # return the standard deviation
    return sum(xy_deviations) / (sqrt(sum(x_sqd_deviations)) * sqrt(sum(y_sqd_deviations)))


gold, silver, bronx = csv_medal_data_parser(3)
testme = average_values(gold, silver, bronx )
