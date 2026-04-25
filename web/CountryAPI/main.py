from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Country API",
    description="A simple API to retrieve and manage country information.",
    version="1.0.0"
)

class Country(BaseModel):
    code: str = Field(..., pattern="^[A-Z]{2}$", description="The 2-letter ISO 3166-1 alpha-2 code of the country.")
    name: str = Field(..., description="The common name of the country.")
    capital: Optional[str] = Field(None, description="The capital city of the country.")
    region: Optional[str] = Field(None, description="The region the country is located in.")
    population: Optional[int] = Field(None, description="The population of the country.")


class Error(BaseModel):
    code: int
    message: str


# This can be replaced with a database or use memory for simplicity.
countries_db = {
    "US": Country(code="US", name="United States", capital="Washington, D.C.", region="Americas", population=331002651),
    "JP": Country(code="JP", name="Japan", capital="Tokyo", region="Asia", population=125800000),
    "IN": Country(code="IN", name="India", capital="New Delhi", region="Asia", population=139340),
    "CA": Country(code="CA", name="Canada", capital="Ottawa", region="Americas", population=380052),
    "DE": Country(code="DE", name="Germany", capital="Berlin", region="Europe", population=83190000),
    "FR": Country(code="FR", name="France", capital="Paris", region="Europe", population=67390000)
}


@app.get("/countries", response_model=List[Country])
def list_countries(
    region: Optional[str] = Query(None, description="Filter countries by region"),
    limit: int = Query(10, description="Maximum number of countries to return"),
    offset: int = Query(0, description="Number of countries to skip")
):
    filtered_countries = list(countries_db.values())
    if region:
        filtered_countries = [c for c in filtered_countries if c.region == region]
    
    return filtered_countries[offset : offset + limit]


@app.post("/countries", response_model=Country, status_code=201)
def add_country(country: Country):
    if country.code in countries_db:
        raise HTTPException(status_code=400, detail="Country already exists")
    countries_db[country.code] = country
    return country


@app.get("/countries/{code}", response_model=Country)
def get_country_by_code(code: str = Path(..., pattern="^[A-Z]{2}$", description="The 2-letter ISO 3166-1 alpha-2 code of the country")):
    country = countries_db.get(code)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@app.put("/countries/{code}", response_model=Country)
def update_country(country: Country, code: str = Path(..., pattern="^[A-Z]{2}$", description="The 2-letter ISO 3166-1 alpha-2 code of the country")):
    if code not in countries_db:
        raise HTTPException(status_code=404, detail="Country not found")
    if country.code != code:
        raise HTTPException(status_code=400, detail="Code in path and body must match")
    countries_db[code] = country
    print(f"Countries DB after update: {countries_db}")
    return country


@app.delete("/countries/{code}", status_code=204)
def delete_country(code: str = Path(..., pattern="^[A-Z]{2}$", description="The 2-letter ISO 3166-1 alpha-2 code of the country")):
    if code not in countries_db:
        raise HTTPException(status_code=404, detail="Country not found")
    del countries_db[code]


@app.patch("/countries/{code}", response_model=Country)
def partial_update_country(code: str, country_update: dict):
    country = countries_db.get(code)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")

    # Validate incoming data for partial update
    # Create a temporary Country object to leverage Pydantic's validation
    # temp_country = Country(**country_update) # This line is not strictly necessary if we validate field by field

    # Update only the fields provided in the request body that are not None
    if country_update.get("name") is not None:
        country.name = country_update["name"]

    if country_update.get("capital") is not None:
        country.capital = country_update["capital"]

    if country_update.get("population") is not None:
        country.population = country_update["population"]
    if country_update.get("region") is not None:
        country.region = country_update["region"]




    countries_db[code] = country
    return country
