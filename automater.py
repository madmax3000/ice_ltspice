import subprocess
#subprocess.run("python run.py")
output_path ="F:\Finalproject\ltspice\ltspice_cli\simulation_parameters.txt"
print(" the optimiser is starting ")
f = open(output_path, 'w+')
f.write("# this is the parameter edit file\n")
f.close
checker = 'y'
while(checker == "y"):

    sotag = input(" plase enter the component name seperated by comas")
    sep_file = sotag.split(",")
    checker = input("do you want to add a new component press y for yes or n for no")
    f = open(output_path, 'a') # make
    if checker == "y":
        f.write("set "+sep_file[0]+" "+sep_file[1])
    else:
        f.write("\nrun " + sep_file[0] + " " + sep_file[1])
    f.close
subprocess.run("python run.py")
