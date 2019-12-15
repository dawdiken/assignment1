from flask import Flask, render_template
import pygal
from models.statistics_generator import average_values, csv_medal_data_parser, max_min_value, variance_std_deviation, correlation

app = Flask(__name__)

# Decorator to tell Flask what URL should trigger our function.
@app.route('/')
def hello_world():
    # Renders html content at the given URL
    return render_template("home.html")

# Decorator to tell Flask what URL should trigger our function.
@app.route('/averageage/')
def average_age():
    try:
        age_column = 3
        gold_medal_val, silver_medal_val, bronze_medal_val = csv_medal_data_parser(age_column)
        list_of_averages_for_all_medals = average_values(gold_medal_val, silver_medal_val, bronze_medal_val)
        age_graph = pygal.Bar()
        age_graph.title = 'Average age of Medal winners'
        age_graph.add('GOLD', [list_of_averages_for_all_medals['Gold']])
        age_graph.add('SILVER', [list_of_averages_for_all_medals['Silver']])
        age_graph.add('BRONZE', [list_of_averages_for_all_medals['Bronze']])
        graph_data_age = age_graph.render_data_uri()

        height_column = 4
        gold_medal_val, silver_medal_val, bronze_medal_val = csv_medal_data_parser(height_column)
        list_of_averages_for_all_medals = average_values(gold_medal_val, silver_medal_val, bronze_medal_val)
        print(list_of_averages_for_all_medals)
        graph_height = pygal.Bar()
        graph_height.title = 'Average Height of Medal winners cm'
        graph_height.add('GOLD', [list_of_averages_for_all_medals['Gold']])
        graph_height.add('SILVER', [list_of_averages_for_all_medals['Silver']])
        graph_height.add('BRONZE', [list_of_averages_for_all_medals['Bronze']])
        graph_data_height = graph_height.render_data_uri()
        return render_template("averageage.html", graph_data_age=graph_data_age, graph_data_height=graph_data_height)
    except Exception as e:
        return str(e)

# Decorator to tell Flask what URL should trigger our function.
@app.route('/maxeage/')
def max_ages():
    # returned tuple for ages
    try:
        age_column = 3
        gold_medal_val, silver_medal_val, bronze_medal_val = csv_medal_data_parser(age_column)
        max_min_age_for_all_medals = max_min_value(gold_medal_val, silver_medal_val, bronze_medal_val)
        max_age, min_age = max_min_age_for_all_medals[0], max_min_age_for_all_medals[1]
        graph = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=6)
        graph.title = 'Max and Min age of Medal winners'
        graph.add('Gold max age', [max_age['Gold']])
        graph.add('Gold min age', [min_age['Gold']])
        graph.add('Silver max age', [max_age['Silver']])
        graph.add('Silver min age', [min_age['Silver']])
        graph.add('Bronze max age', [max_age['Bronze']])
        graph.add('Bronze min age', [min_age['Bronze']])
        graph_data = graph.render_data_uri()
        return render_template("maxage.html", graph_data=graph_data, gold_max=max_age['Gold'], gold_min=min_age['Gold'],
                               silver_max=max_age['Silver'], silver_min=min_age['Silver'],
                               bronze_max=max_age['Bronze'], bronze_min=min_age['Bronze'])
    except Exception as e:
        return str(e)

# Decorator to tell Flask what URL should trigger our function.
@app.route('/correlation/')
def correlation_stat():
    try:
        ageColumnNumber = 3
        heightColumnNumber = 4
        age_gold_medal_val, age_silver_medal_val, age_bronze_medal_val = csv_medal_data_parser(ageColumnNumber)
        height_gold_medal_val, height_silver_medal_val, height_bronze_medal_val = csv_medal_data_parser(
            heightColumnNumber)
        correlation_gold = f"{correlation(age_gold_medal_val, height_gold_medal_val):.4f}"
        correlation_silver = f"{correlation(age_silver_medal_val, height_silver_medal_val):.4f}"
        correlation_bronze = f"{correlation(age_bronze_medal_val, height_bronze_medal_val):.4f}"
        return render_template("correlation.html", correlation_gold=correlation_gold,
                               correlation_silver=correlation_silver,
                               correlation_bronze=correlation_bronze)
    except Exception as e:
        return str(e)

# Decorator to tell Flask what URL should trigger our function.
@app.route('/variabilityage/')
def variability_age():
    try:
        age_column = 3
        gold_medal_val, silver_medal_val, bronze_medal_val = csv_medal_data_parser(age_column)
        mean_age_medal_winners = average_values(gold_medal_val, silver_medal_val, bronze_medal_val)
        variance_of_medal_winners, std_deviation_medal_winners = variance_std_deviation(gold_medal_val, silver_medal_val
                                                                                        , bronze_medal_val)

        gold_mean, silver_mean, bronze_mean = mean_age_medal_winners['Gold'], \
                                              mean_age_medal_winners['Silver'], \
                                              mean_age_medal_winners['Bronze']

        gold_variance, silver_variance, bronze_variance = variance_of_medal_winners['Gold'], \
                                                          variance_of_medal_winners['Silver'], \
                                                          variance_of_medal_winners['Bronze']

        gold_std_dev, silver_std_dev, bronze_std_dev = std_deviation_medal_winners['Gold'], \
                                                       std_deviation_medal_winners['Silver'], \
                                                       std_deviation_medal_winners['Bronze']

        # gold medal graph
        gold_graph = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=3)
        gold_graph.title = 'Gold Medal winners age Mean, Variance and Std. deviation values'
        gold_graph.add('Gold mean age', [mean_age_medal_winners['Gold']])
        gold_graph.add('Gold variance in age', [variance_of_medal_winners['Gold']])
        gold_graph.add('Gold Std. deviation in age', [std_deviation_medal_winners['Gold']])
        graph_data_gold = gold_graph.render_data_uri()

        # silver medal graph
        silver_graph = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=3)
        silver_graph.title = 'Silver Medal winners age Mean, Variance and Std. deviation values'
        silver_graph.add('Silver mean age', [mean_age_medal_winners['Silver']])
        silver_graph.add('Silver variance in age', [variance_of_medal_winners['Silver']])
        silver_graph.add('Silver Std. deviation in age', [std_deviation_medal_winners['Silver']])
        graph_data_silver = silver_graph.render_data_uri()

        # bronze medal graph
        bronze_graph = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=3)
        bronze_graph.title = 'Bronze Medal winners age Mean, Variance and Std. deviation values'
        bronze_graph.add('Bronze mean age', [mean_age_medal_winners['Bronze']])
        bronze_graph.add('Bronze variance in age', [variance_of_medal_winners['Bronze']])
        bronze_graph.add('Bronze Std. deviation in age', [std_deviation_medal_winners['Bronze']])
        graph_data_bronze = bronze_graph.render_data_uri()
        return render_template("variabilityage.html", graph_data_gold=graph_data_gold,
                               graph_data_silver=graph_data_silver,
                               graph_data_bronze=graph_data_bronze,
                               gold_mean=f"{gold_mean:.2f}", silver_mean=f"{silver_mean:.2f}",
                               bronze_mean=f"{bronze_mean:.2f}",
                               gold_variance=f"{gold_variance:.2f}", silver_variance=f"{silver_variance:.2f}",
                               bronze_variance=f"{bronze_variance:.2f}",
                               gold_std_dev=f"{gold_std_dev:.2f}", silver_std_dev=f"{silver_std_dev:.2f}",
                               bronze_std_dev=f"{bronze_std_dev:.2f}")
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
