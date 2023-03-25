def all_command():
    """
    cse_finance's all current available commands
    
    Command      | Variables                                    | Description
    ==================================================================================================================
    get_price    | index_symbol: str                            | The function returns the corresponding financial of
                        Symbol representing a index on CSE.       a given stock symbol and a period. The function
                    start: str                                    returns a dataframe that includes Date, Close,
                        Download start date string (YYYY-MM-DD).  Quantity and Volume.
                        Default is 1929-01-01.
                    end: str
                        Download end date string (YYYY-MM-DD).
                        Default is the current day.
    
    get_index    | index_symbol: str                            | Function returns a dataframe corresponding MASI and
                        Symbol representing a index on CSE.       MADEX values of a given index symbol and a period.
                    start: str                                     
                        Download start date string (YYYY-MM-DD).  
                        Default is 1929-01-01.
                    end: str
                        Download end date string (YYYY-MM-DD).
                        Default is the current day.
                    period: str
                        Default is one month.
    
    get_info     | ticker: str                                  | Function returns financial information of a company.
                        Stock's ticker symbol.
                   year: str
                       Returns the results of a selected year.
                       Default is None
    
    stats        | None                                         | Return technical indicators.
    
    get_tickers  | None                                         | Function returns all current listed companies
                                                                  at the CSE.
                                                                  
    all_command  | None                                         | cse_finance's current available commands.                                                             
    """
    
    return print(all_command.__doc__)
