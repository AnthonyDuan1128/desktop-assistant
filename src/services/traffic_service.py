import requests
import logging

class TrafficService:
    def __init__(self):
        pass

    def get_traffic_info(self, location):
        logging.info(f"Fetching traffic information for {location}")
        url = f"https://api.trafficservice.com/location/{location}"  # Example API endpoint
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error("Failed to fetch traffic information")
            raise Exception("Failed to fetch traffic information")

    def display_traffic_info(self, traffic_data):
        # Placeholder for method to display traffic information in the UI
        pass