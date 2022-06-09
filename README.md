
# US Bikeshare Data Exploration

This is a simple Python script that receives input via a terminal to create an
interactive experience to explore some descriptive statistics about
bikeshare datasets from 3 different US cities.

## Table of Contents

* [Software](#software)
* [Files](#files)
* [Questions](#questions)
* [Instructions](#instructions)
* [Creator](#creator)

## Software

* Python 3, NumPy, and Pandas installed using Anaconda.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

## Files

- **bikeshare.py:** A file containing the Python code used to run the interactive explorer.
- **chicago.csv, new_york_city.csv, washington.csv:** Three csv datasets that contain randomly selected data for the first six months of 2017. Columns include:

    - Start Time (e.g., 2017-01-01 00:07:57)
    - End Time (e.g., 2017-01-01 00:20:53)
    - Trip Duration (in seconds - e.g., 776)
    - Start Station (e.g., Broadway & Barry Ave)
    - End Station (e.g., Sedgwick St & North Ave)
    - User Type (Subscriber or Customer)
    ---
  The Chicago and New York City files also have the following two columns:
    - Gender
    - Birth Year

## Questions

**#1 Popular times of travel (i.e., occurs most often in the start time)**

 - most common month
 - most common day of week
 - most common hour of day

**#2 Popular stations and trip**

 - most common start station
 - most common end station
 - most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

 - total travel time
 - average travel time

**#4 User info**

 - counts of each user type
 - counts of each gender (only available for NYC and Chicago)
 - earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Instructions

* Open the terminal app in this directory, then run `python bikeshare.py`.

## Creator

* Iman El-Ganzoury
    - [https://github.com/Iman-ElGanzoury](https://github.com/Iman-ElGanzoury)
