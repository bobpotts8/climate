import netCDF4 as nc
import numpy as np

def find_nan_values(nc_file, variable_name):
    try:
        # Open the NetCDF file in read mode
        dataset = nc.Dataset(nc_file, 'r')

        # Check if the variable exists in the file
        if variable_name in dataset.variables:
            # Get the variable data
            variable = dataset.variables[variable_name][:]
            
            # Find NaN values
            nan_indices = np.isnan(variable)
            
            if np.any(nan_indices):
                nan_indices = np.where(nan_indices)
                print(f"NaN values found in '{variable_name}' variable at indices: {nan_indices}")
            else:
                print(f"No NaN values found in '{variable_name}' variable.")
        else:
            print(f"Variable '{variable_name}' not found in the NetCDF file.")

        # Close the NetCDF file
        dataset.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    nc_file = '/Users/bobpotts/Desktop/Transfers/Climate Test/daily_data_tester.nc'  # Replace with the path to your NetCDF file
    variable_name = 'tos'  # Replace with the name of your variable
    find_nan_values(nc_file, variable_name)