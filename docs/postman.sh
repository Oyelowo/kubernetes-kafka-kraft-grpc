# Get user 1
curl -X GET "http://localhost:30001/api/persons/1" -H "accept: application/json"

# Get all connections for person 1 between date
curl -X GET "http://localhost:30001/api/persons/1/connection?distance=5&end_date=2022-10-01&start_date=2020-01-01" -H "accept: application/json"

# Create new person
curl -X POST -H "Content-Type: application/json" \
 -d '{"first_name": "Oyelowo","last_name":"Oyedayo", "company_name":"Blayz"}' \
"http://localhost:30001/api/persons"

# Create location. This sends the location to kafka via the api and the 
# location service subscribes to the location topics to save incoming location to its postgres
curl -X POST -H "Content-Type: application/json" \
 -d '{"person_id": 1,"longitude":"24.9384", "latitude":"60.1699"}' \
"http://localhost:30001/api/locations"

# You can also send plenty location data for testing:
for i in {1..10000}
    do
    # your-unix-command-here
    echo $i
    curl -X POST -H "Content-Type: application/json" \
    -d '{"person_id": 3,"longitude":"24.9384", "latitude":"60.1699"}' \
    "http://localhost:30001/api/locations"
done
