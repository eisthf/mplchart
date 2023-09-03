""" sample script to render a chart to svg """

import yfinance as yf

from mplchart.chart import Chart

from mplchart.primitives import Candlesticks, Volume
from mplchart.indicators import SMA, RSI, MACD


def main():
    ticker = 'AAPL'
    prices = yf.Ticker(ticker).history('5y')

    max_bars = 250
    indicators = [Candlesticks(), SMA(50), SMA(200), Volume(), RSI(), MACD()]
    chart = Chart(title=ticker, max_bars=max_bars)
    chart.plot(prices, indicators)

    data = chart.render('svg')
    print(data[:256], "...")


if __name__ == "__main__":
    main()
