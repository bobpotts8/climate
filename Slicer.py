
import xarray as xr

# Load the NetCDF file
ds = xr.open_dataset('/Users/bobpotts/Desktop/Transfers/Climate_Test/Daily_data_copy.nc')

# Define the start and end dates for your slice
start_date = '1990-01-01'  # Replace with your start date
end_date = '2023-10-10'    # Replace with your end date

# Slice the data using the sel method
ds_slice = ds.sel(time=slice(start_date, end_date))

print(ds_slice)