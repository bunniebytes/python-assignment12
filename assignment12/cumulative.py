import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from contextlib import closing

# Task 2
with closing(sqlite3.connect("../db/lesson.db")) as conn:
	print("Database successfully opened")
	conn.execute("PRAGMA foreign_keys = 1")

	query = """SELECT
					li.order_id,
					sum(li.quantity * p.price) AS total_price
				FROM line_items AS li
				JOIN products AS p
					ON li.product_id = p.product_id
				GROUP BY li.order_id"""
	
	df = pd.read_sql(query, con = conn)
	def cumulative(row):
		totals_above = df['total_price'][0:row.name+1]
		return totals_above.sum()

	df['cumulative'] = df.apply(cumulative, axis=1)
	
	df.plot(x = "order_id", y = "cumulative", kind = "line", title = "Cumulative Revenue vs Order ID")
	plt.show()