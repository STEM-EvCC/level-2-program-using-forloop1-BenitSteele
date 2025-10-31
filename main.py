mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
number_of_names = len(mission_names) # Making sure the names of the mission are seen as a length
successful_missions = len(mission_success) # Making sure the successfulness of the missions are seen as a length
number_of_years = len(mission_years)
print(f"Total number of missions: {number_of_names}") # Telling us how many total missions there were
item_to_count = True # Having the code store our true values 
count = mission_success.count(item_to_count) # Having the code look for "True" items only
print(f"Number of successful missions: {count}") # Seeing how many "True" successes we have
percentage_success = (count / successful_missions) * 100 
percentage_rounded = round(percentage_success, 2)
print(f"Success rate: {percentage_rounded}%") # Percentage of the success rate from how many "True" items we had in successful missions
print("Missions launched before the year 2000:")

for i in range(len(mission_names)): # Looking within the names list as a range to check the names as we check the year
    if mission_years[i] < 2001:  # Checking the year if it's before 2000
        print(f"- {mission_names[i]}") # If the condition is before 2000 it'll print the name that is lined up with the year at the time





