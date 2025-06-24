#!/usr/bin/python3

gamers = []

def add_gamer(gamer, gamers_list):
    if not 'name' in gamer:
        print('No name key in gamer dictionary')
        return
    if not 'availability' in gamer:
        print('No availability list in gamer dictionary')
        return
    # Append gamer dict to gamer's list
    gamers_list.append(gamer)

kimberly = {'name': 'Kimberly Warner', 
            'availability': ['Monday', 'Tuesday', 'Friday'] }  

add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


def build_daily_frequency_table():
    return {'Monday': 0, 'Tuesday': 0, 
            'Wednesday': 0, 'Thursday': 0, 
            'Friday': 0, 'Saturday': 0, 'Sunday': 0 }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1
    return available_frequency

results_frequency = calculate_availability(gamers, count_availability)
print(results_frequency)    

def find_best_night(availability_table):
    return max(availability_table.items(), key=lambda x: x[1])

game_night = find_best_night(results_frequency)
print(f'Games night is: {game_night[0]}.')
