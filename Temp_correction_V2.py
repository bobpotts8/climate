import numpy as np
from netCDF4 import Dataset

# Function to apply the linear temperature correction to both hemispheres
def apply_temperature_correction(input_file, output_file, northern_correction, southern_correction):
    # Open the input NetCDF file
    input_dataset = Dataset(input_file, 'r')

    # Create a copy of the input dataset as the output dataset
    output_dataset = Dataset(output_file, 'w')

    # Loop through variables in the input dataset
    for var_name, var in input_dataset.variables.items():
        # Copy variable metadata to the output dataset
        out_var = output_dataset.createVariable(var_name, var.dtype, var.dimensions)
        out_var.setncatts({k: var.getncattr(k) for k in var.ncattrs()})

        if 'latitude' in var.dimensions:
            latitude = input_dataset.variables['latitude'][:]

            # Apply corrections based on hemisphere
            northern_indices = latitude >= 0
            southern_indices = latitude < 0

            out_var[:] = np.where(northern_indices, var[:] + northern_correction * latitude, var[:])
            out_var[:] = np.where(southern_indices, var[:] + southern_correction * latitude, out_var[:])
        else:
            out_var[:] = var[:]

    # Close the datasets
    input_dataset.close()
    output_dataset.close()



if __name__ == '__main__':
    input_file = '/Users/bobpotts/Desktop/Transfers/Climate_Test/daily_data_copy.nc'
    output_file = '/Users/bobpotts/Desktop/Transfers/Climate_Test/output_data.nc'
    northern_correction = -0.458  # Correction factor for the Northern Hemisphere
    southern_correction = -0.190  # Correction factor for the Southern Hemisphere

    apply_temperature_correction(input_file, output_file, northern_correction, southern_correction)