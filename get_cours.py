import requests

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def update_course(base="EUR"):
    url = NBU_API_URL
    params = {"base": base}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    usd = [item for item in data if item.get("cc") == "USD"] 
    eur = [item for item in data if item.get("cc") == "EUR"] 
    gbp = [item for item in data if item.get("cc") == "GBP"] 
    
    usd_rate = usd[0]["rate"] if usd else None
    eur_rate = eur[0]["rate"] if eur else None
    gbp_rate = gbp[0]["rate"] if gbp else None

    return [usd_rate, eur_rate, gbp_rate]       
