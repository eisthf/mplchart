""" sample script to display a chart in a popup window """


from mplchart.chart import Chart
from mplchart.helper import get_prices

from mplchart.primitives import Candlesticks, Volume
from mplchart.indicators import SMA, RSI, MACD


def main():
    ticker = 'AAPL'
    prices = get_prices(ticker)

    max_bars = 250
    indicators = [Candlesticks(), SMA(50), SMA(200), Volume(), RSI(), MACD()]
    chart = Chart(title=ticker, max_bars=max_bars)
    chart.plot(prices, indicators)
    chart.show()


if __name__ == "__main__":
    main()
