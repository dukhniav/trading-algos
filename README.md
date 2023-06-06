# trading-algos
## Setup
### Recommend using [venv](https://docs.python.org/3/library/venv.html)
- Create a virtual environment
```console
python3 -m venv <env_name>
```
- Activate venv
```console
source <env_name>/bin/activate
```
- Deactivate venv
```console
deactivate
```

### Install required dependencies
```console
pip install -r requirements.txt
```

#### To upgrade your installed packages
```console
pip install --upgrade -r requirements.txt
```

## Setup/retrieve alpha vantage credentials
1. Go to https://www.alphavantage.co/support/#api-key
2. Fill out required fields
3. Get api key

Once the developer credentials are availabl, run setup `setup.py` file

It will loop through and set the required credentials in a `.env` file

If a single credential needs to be updated, run `setup.py` file with one of the following as a parameter:
- `alpha_vantage_api`

## Using alpha vantage API

### Intraday API Parameters

- Required: `function`
	- The time series of your choice. In this case, `function=TIME_SERIES_INTRADAY`
- Required: `symbol`
	- The name of the equity of your choice. For example: `symbol=IBM`
- Required: `interval`
	- Time interval between two consecutive data points in the time series. The following values are supported: 
		- `1min`
		- `5min`
		- `15min`
		- `30min`
		- `60min`
- Optional: `adjusted`
	- By default, `adjusted=true` and the output time series is adjusted by historical split and dividend events. 
	- Set `adjusted=false` to query raw (as-traded) intraday values.
- Optional: `outputsize`
	- By default, `outputsize=compact`. 
	- Strings compact and full are accepted with the following specifications: 
		- `compact` returns only the latest 100 data points in the intraday time series
		- `full` returns the full-length intraday time series. 
	- The "compact" option is recommended if you would like to reduce the data size of each API call.
- Optional: `datatype`
	- By default, `datatype=json`. 
	- Strings json and csv are accepted with the following specifications: 
		- `json` returns the intraday time series in JSON format; 
		- `csv` returns the time series as a CSV (comma separated value) file.
- Required: `apikey`
	- Your API key.
- Possible URL
	- `url = f"https://www.alphavantage.co/query?function={FUNCTION}&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}"`

### Alpha vantage documentation
- https://www.alphavantage.co/documentation/
