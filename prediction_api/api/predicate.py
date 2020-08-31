import requests


def get_current_values():
    url = "https://oln86130.live.dynatrace.com/api/v1/timeseries/?relativeTime=hour&Api-Token=40-viy3kSyKZItDYZmAfm&aggregationType=COUNT&entity=APPLICATION-294916C9639A9385&timeseriesId=com.dynatrace.builtin:app.useractionsperminute"
    data = requests.get(url)
    return data
