
from teamsInitializer.initializeTeams import fetchMLBTeams
from scheduleUpdater.fetchCurrentSchedule import fetchAndUpdateCurrentSchedule
from scheduleUpdater.fetchPastSchedule import fetchAndUpdateOldSeason
import logging
import os 


# Set up basic configuration
logging.basicConfig(
    filename='app.log',
    filemode='w', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

current_season = os.getenv("CURRENT_SEASON")
base_url = os.getenv("MLB_API_BASE_URL")

def main():
    print('here inside main')
    fetchMLBTeams()
    old_seasons = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
    for season in old_seasons:
        fetchAndUpdateOldSeason(season, base_url)
    fetchAndUpdateCurrentSchedule(current_season, base_url)

if __name__ == "__main__":
    main()