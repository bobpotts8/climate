import netCDF4 as nc

def print_variable_values(nc_file, variable_name):
    try:
        # Open the NetCDF file in read mode
        dataset = nc.Dataset(nc_file, 'r')

        # Check if the variable exists in the file
        if variable_name in dataset.variables:
            # Get the variable data
            variable = dataset.variables[variable_name][:]

            # Print every value
            for value in variable:
                print(value)
        else:
            print(f"Variable '{variable_name}' not found in the NetCDF file.")

        # Close the NetCDF file
        dataset.close()
    except Exception as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    nc_file = '/Users/bobpotts/Desktop/Transfers/Climate_Test/daily_data_tester.nc'  # Replace with the path to your NetCDF file
    variable_name = 'tos'  # Replace with the name of your variable
    print_variable_values(nc_file, variable_name)