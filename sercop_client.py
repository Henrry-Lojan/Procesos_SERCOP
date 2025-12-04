import requests
import datetime

class SercopClient:
    BASE_URL = "https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api"

    def search_processes(self, keyword, year=None, page=1):
        """
        Search for procurement processes by keyword.
        """
        if year is None:
            year = datetime.datetime.now().year
        
        params = {
            "year": year,
            "search": keyword,
            "page": page
        }
        
        try:
            response = requests.get(f"{self.BASE_URL}/search_ocds", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def get_process_details(self, ocid):
        """
        Get details for a specific process by OCID.
        """
        params = {"ocid": ocid}
        try:
            response = requests.get(f"{self.BASE_URL}/record", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching details: {e}")
            return None
