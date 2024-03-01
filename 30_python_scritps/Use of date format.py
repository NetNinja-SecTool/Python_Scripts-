from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)
