import xarray as xr
import pandas as pd

# Load the input NetCDF file with monthly data
input_file = '/Users/bobpotts/Desktop/Climate Test/Adjusted_SST.nc'
ds = xr.open_dataset(input_file)

# Create a date range for the daily data
start_date = pd.Timestamp(ds.time.min().values)
end_date = pd.Timestamp(ds.time.max().values)
daily_dates = pd.date_range(start_date, end_date, freq='D')

# Interpolate the data to daily resolution
ds_daily = ds.reindex(time=daily_dates, method='ffill')  # Using forward fill for interpolation

# Save the result to a new NetCDF file
output_file = '/Users/bobpotts/Desktop/Climate Test/daily_data.nc'
ds_daily.to_netcdf(output_file)