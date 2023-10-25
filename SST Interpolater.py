import netCDF4 as nc
import numpy as np
from scipy import interpolate

def interpolate_variable(nc_file, variable_name):
    try:
        # Open the NetCDF file in read-write mode
        dataset = nc.Dataset(nc_file, 'r+')

        # Check if the variable exists in the file
        if variable_name in dataset.variables:
            # Get the variable data
            variable = dataset.variables[variable_name][:]
            
            # Create an array of indices matching the shape of the variable
            indices = np.arange(variable.shape[0])

            # Get the indices of missing values
            missing_indices = np.where(variable.mask)[0]

            # Create an interpolating function
            interpolator = interpolate.interp1d(indices[~variable.mask], variable[~variable.mask], kind='linear', fill_value='extrapolate')

            # Interpolate missing values
            variable[missing_indices] = interpolator(missing_indices)

            # Update the variable in the NetCDF file
            dataset.variables[variable_name][:] = variable

            print(f"Interpolation completed for '{variable_name}' variable.")
        else:
            print(f"Variable '{variable_name}' not found in the NetCDF file.")

        # Close and save the NetCDF file
        dataset.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    nc_file = '/Users/bobpotts/Desktop/Transfers/Climate_Test/daily_data_tester.nc'  # Replace with the path to your NetCDF file
    variable_name = 'tos'  # Replace with the name of your variable
    interpolate_variable(nc_file, variable_name)