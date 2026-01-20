# messing-around

## [Clean-Structure.py](https://github.com/Tyler-Barsby/messing-around/blob/c4eebde8afb0e8c036aa0ecc1b50552da4895bad/Clean-Structure.py)

The purpose of this script is scan file names and rename them according to a set **naming convention**.

#### get_target_folders()
The below function reads the **[folders.md](https://github.com/Tyler-Barsby/messing-around/blob/c4eebde8afb0e8c036aa0ecc1b50552da4895bad/folders.md)** file and determines which sub-directories to open and clean. 
![get target folders function](/Assets/get_target_folders.png "get_target_folders function")

#### clean_files_in_targets()
This function uses the array from the previous function to iterate through and rename the files within to the set convention.
![get target folders function](/Assets/clean_files_in_targets.png "clean_files_in_targets")

