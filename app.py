from get_sports import get_fixtures

url = "https://www.tvsportguide.com"
fixtures = get_fixtures(url)
for fixture in fixtures:
    print(fixture, fixtures[fixture], "\n\n")