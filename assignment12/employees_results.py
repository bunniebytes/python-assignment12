import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from contextlib import closing

with closing(sqlite3.connect("../db/lesson.db")) as conn:
	print("Database successfully opened")
	conn.execute("PRAGMA foreign_keys = 1")
	cursor = conn.cursor()

	# Task 1
	query = """SELECT
				last_name,
				SUM(price * quantity) AS revenue
    		FROM employees AS e
      		JOIN orders AS o
        		ON e.employee_id = o.employee_id
         	JOIN line_items l
          		ON o.order_id = l.order_id
            JOIN products p
            	ON l.product_id = p.product_id
            GROUP BY e.employee_id;"""
	df = pd.read_sql(query, con = conn)
	
	df.plot(x = "last_name", y = "revenue", kind = "bar", title = "Revenue made by Employees")
	plt.show()