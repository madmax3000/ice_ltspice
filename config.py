##########################################
## CONFIGURATION OF LTspice SIMULATIONS ##
##########################################
import subprocess
# File path of the LTspice program installed on the system
LTSpice_executable_path = 'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe' # works on windows only with 17th version of ltspice
# The name of the circuit to be used in simulations
LTSpice_asc_filename ='showfile.asc'

# The measurements to be saved from the simulation. The appropriate numbers can be found in the .raw file generated at simulation.
variable_numbering = {'time': 0, 'n002': 2, 'R3': 3}
#{'the raw file variable name' : raw variable index, 'the raw file variable name' : raw vari index,}
# raw file index starting from 1, 2 ,3 etc
''' the time variable is :0 it is default as it is defined by the program,  the variable name 'noo2' is representing the variable names : the comming number which is indexed" 
"represents the the indexing of the raw file variable starting from the counting number 1, 2, 3 etc" 
"this reperesnts which data from raw file is to be saved into the csv file for further processing " '''
# The ordering of the measurements to be saved in the output csv files can be changed below, by changing how the numbers are ordered.
# E.g. switch place of 0 and 1 if you want V_c to be placed left of time in the output csv files.
preffered_sorting = [0, 1, 2]
# the plotting would have 0 for time , 1 for voltages or  2 for currents etc

# Leave blank if output should be writtten to root folder. The folder specified must be created manually if it doesn't exist.
output_data_path = "data"
# Naming convention for output files. Can be numerical names, increasing in value as output is created.
# Parameter names gives the files the name of the parameter that it is run with.
# Assumes number by default. Set to 'parameter' or 'number'.
output_data_naming_convention = 'number'
#for encoding related data use AScii mode of compression for ltspice
