import netCDF4 as nc

def check_variables(nc_file):
    try:
        # Open the NetCDF file
        dataset = nc.Dataset(nc_file, 'r')

        # Get a list of variable names in the file
        variable_names = dataset.variables.keys()

        print(f"Variable checks for {nc_file}:")
        
        for var_name in variable_names:
            variable = dataset.variables[var_name]
            
            # Check for variable dimensions
            dimensions = variable.dimensions
            if dimensions:
                print(f"Variable '{var_name}' dimensions: {', '.join(dimensions)}")
            else:
                print(f"Variable '{var_name}' has no dimensions.")
            
            # Check for variable shape
            shape = variable.shape
            print(f"Variable '{var_name}' shape: {shape}")
            
            # Check for variable attributes
            attributes = variable.ncattrs()
            if attributes:
                print(f"Variable '{var_name}' attributes:")
                for attr_name in attributes:
                    attr_value = variable.getncattr(attr_name)
                    print(f"  {attr_name}: {attr_value}")
            else:
                print(f"Variable '{var_name}' has no attributes.")
                
            print()  # Add a blank line between variables

        # Close the NetCDF file
        dataset.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    nc_file = '/Users/bobpotts/Desktop/Transfers/Climate Test/daily_data_tester.nc'  # Replace with the path to your NetCDF file
    check_variables(nc_file)