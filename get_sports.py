import requests
from bs4 import BeautifulSoup


def get_content(url):
    '''
    takes in url and outputs iterator object of the required content
    '''
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="match-container")

    day_elements = results.find_all("div", class_="day")

    return day_elements

def get_fixtures(url):
    day_elements = get_content(url)
    day_count = 0
    matches = {}
    accepted_sports = {'NBA', 'NFL', 'MMA', "Euro 2024", "Formula 1", "Premier League", "Champions League"}

    for day in day_elements:
        indexes = set()
        if day_count < 7:
            day_count += 1
            day_title = day.find("strong", class_="day-date")

            match_detail_elements = day.find_all("div", class_="match-detail")
            for i, match in enumerate(match_detail_elements):
                match_sport = match.find("a").text.strip()
                # a few times match_sport will not be right
                if match_sport == "· Bet365 Live odds":
                    #in these cases, this code retrieves the right string for match_sport
                    match_sport = match.find("p").text[:-35].strip()
                if match_sport in accepted_sports:
                    match_title = match.find("h3").text
                    if day_title.text in matches:
                        matches[day_title.text].append([match_title, match_sport])
                    else:
                        matches[day_title.text] = [[match_title, match_sport]]                      
                    indexes.add(i)

            match_info_elements = day.find_all("div", "match-info")
            index = 0
            for j, match in enumerate(match_info_elements):
                if j in indexes:
                    match_time = match.find("div", class_="match-time")
                    matches[day_title.text][index].append(match_time.text)
                    index += 1
        else:
            break
    return matches
    