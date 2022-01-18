from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value) 
	frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
# Below must be wrapped in brackets because the data set has multiple elements
data = [Bar(x=x_values, y=frequencies)]

# There are many option to customize the axes, all of which you use
#	by storing your option in a dictionary. Here we only use the title option
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D10 50,000 times', 
				xaxis=x_axis_config, yaxis=y_axis_config)
#Creates an html file and accepts a dictionary
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')






























