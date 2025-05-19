from service import api_service

def get_user_details():
    users = api_service.get_users()
    number = users['number']
    print(f'Il y à actuellement {number} personne dans l"espace')
    for person in users['people']:
        print(f"{person['name']} est à bord.")

def get_location_details():
    location = api_service.get_location()
    latitude = location['iss_position']['latitude']
    longitude = location['iss_position']['longitude']
    print(f"Position actuelle de l'ISS : Latitude : {latitude}, Longitude : {longitude}")

def main():
    get_user_details()
    get_location_details()

if __name__ == "__main__":
    main()