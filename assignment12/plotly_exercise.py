import plotly.express as px
import plotly.data as pldata

# Task 3
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

def convert_to_float(string):
	if "-" in string:
		temp = [float(x) for x in string.split("-")]
		return sum(temp)/len(temp)
	else:
		return float(string.replace("+", ""))

df["strength"] = df["strength"].apply(convert_to_float)

fig = px.scatter(df, x = "strength", y = "frequency", color = "direction", title = "Wind Strength versus Frequency", hover_data= ["direction", "strength", "frequency"])

fig.write_html("wind.html", auto_open = True)