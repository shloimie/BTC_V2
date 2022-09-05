import pandas as pd
import matplotlib.pyplot as plt


# reading the database2
data = pd.read_csv("output.csv")
print(data)

# Scatter plot with day against tip
# plt.plot(data['time'])
# plt.plot(data['price'])
plt.plot_date(data['time'],data['price'])
plt.gcf().autofmt_xdate()

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

plt.show()

