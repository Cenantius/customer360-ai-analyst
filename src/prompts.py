DATABASE_SCHEMA = """
You are working with an SQLite database called Customer360.

Available view:

1. customer_lifetime_value
Columns:
- customer_id: unique customer identifier
- first_name: customer's first name
- last_name: customer's last name
- email: customer's email address
- city: customer's city
- completed_orders: number of completed orders
- total_completed_revenue: total revenue from completed orders

Use customer_lifetime_value when the user asks about:
- best customers
- highest value customers
- lifetime value
- total revenue by customer
- most valuable customers
"""