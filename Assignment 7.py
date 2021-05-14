#Alex Hanna
#Assignment 7, CIS 245
#04/27/2021
# Dictionary with stock ticker and stock price, user enters ticker symbol and price is displayed


stock_dict = {
    'GOOGL':'$1000',
    'TSLA':'$2000',
    'AMZN':'$3000',
    'AAPL':'$200',
    'MSFT':'$2500',
    'DELL':'$60',
    'SNE':'$450',
    'TGT':'$85',
    'CAT':'$45',
    'LOW':'$600',
}
#dictionary created with ticker symbol as key and prices as the values

ticker = input("Enter the stock's ticker symbol:")

if ticker in stock_dict:
    # if condition that checks to see if input is a key in stock_dict

    print(f'The stock price for {ticker} is {stock_dict[ticker]}')
    #prints ticker symbol with corresponding value from stock_dict

else:
    print('Sorry, that ticker symbol was not found')
#else condition will print error message if ticker symbol is not in stock_dict