import os
import requests

mock_data_endpoint = "https://gist.githubusercontent.com/mikeonslow/a95b3ba5bf28fcbfc81c40916be06db6/raw/dd5a41daf1c8842cbcc444c20ae7241ba52ebc6c/mike_onslow_linkedin.json"
linkedin_profile_url = "https://www.linkedin.com/in/mikeonslow/"


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape linkedin profile and return the profile as a dictionary"""

    # response = get_data(True)  # MOCK DATA
    response = get_data() # Live data

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


def get_data(isMock=False):
    if isMock:
        response = requests.get(mock_data_endpoint)
    else:
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            "https://nubela.co/proxycurl/api/v2/linkedin",
            params={"url": linkedin_profile_url},
            headers=header_dic,
        )

    return response
