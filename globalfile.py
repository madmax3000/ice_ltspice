import config
diagramarray=[config.LTSpice_asc_filename] #csv file
paramsarray=['simulation_parameters.txt']  #params file is read here #not used now a days
outputarray=[(config.output_data_path + ".csv")] # output file details are sent here
# all csv files should be in the same order params as well as diagram all files must be mentioned in same order
controlvariable=[] #can be added as list