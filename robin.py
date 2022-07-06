import requests

robin_api_base_url = 'https://api.robinpowered.com/v1.0/'

def get_headers(access_token):
    return {
    "Accept": "application/json",
    "Authorization": f"Access-Token {access_token}"
}

def get_locations(access_token, organisation_id):
    url = f"{robin_api_base_url}organizations/{organisation_id}/locations/?&page=1&per_page=100"
    headers = get_headers(access_token)

    return {location['name']: {'id': location['id'], 'timezone': location['time_zone']} for location in requests.get(url, headers=headers).json()['data']}

def get_emails(location_id, start, end, access_token):
    headers = get_headers(access_token)
    emails = get_reservations(location_id, start, end, headers)
    unique_emails = list(set(emails))
    return unique_emails

def get_reservations(location_id, start, end, headers):
    spaces = get_spaces_in_location(location_id, headers)
    space_emails = [get_emails_in_space(space, start, end, headers) for space in spaces]
    space_emails_flat = [j for i in space_emails for j in i]
    return space_emails_flat
    

def get_spaces_in_location(location_id, headers):
    url = f"{robin_api_base_url}locations/{location_id}/spaces/?&page=1&per_page=500"
    return [space['id'] for space in requests.get(url, headers=headers).json()['data']]

def get_emails_in_space(space_id, start, end, headers):
    url = f"{robin_api_base_url}reservations/seats/?space_ids={space_id}&types=hot,assigned,hoteled&page=1&per_page=500&before={end}&after={start}"
    return [reservation['reservee']['email'] for reservation in requests.get(url, headers=headers).json()['data']]