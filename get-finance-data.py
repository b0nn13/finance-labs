# Define the ticker list
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers_list = ['LREN3.SA', 'PETR4.SA', 'MGLU3.SA', 'NATU3.SA']
# Import pandas
data = pd.DataFrame(columns=tickers_list)
# Fetch the data
for ticker in tickers_list:
 data[ticker] = yf.download(ticker,period="max")['Adj Close']
 # Print first 5 rows of the data
data.head()

# Plot all the close prices
((data.pct_change()+1).cumprod()).plot(figsize=(10, 7))
# Show the legend
plt.legend()
# Define the label for the title of the figure
plt.title('Preço de Fechamento Ajustado', fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Preço', fontsize=14)
plt.xlabel('Ano', fontsize=14)
# Plot the grid lines
plt.grid(which='major', color='k', linestyle='-.', linewidth=0.5)
plt.show()