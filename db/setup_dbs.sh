# Usage: pass in the DB container ID as the argument

# Set database configurations
export PERSON_CT_DB_USERNAME=ct_admin
export PERSON_CT_DB_NAME=person


cat ./db/2020-08-15_init-db-person.sql | kubectl exec -i postgres-person-0 -- bash -c "psql -U $PERSON_CT_DB_USERNAME -d $PERSON_CT_DB_NAME"

cat ./db/udaconnect_public_person.sql | kubectl exec -i postgres-person-0 -- bash -c "psql -U $PERSON_CT_DB_USERNAME -d $PERSON_CT_DB_NAME"



# Usage: pass in the DB container ID as the argument

# Set database configurations
export LOCATION_CT_DB_USERNAME=ct_admin
export LOCATION_CT_DB_NAME=location


cat ./db/2020-08-15_init-db-location.sql | kubectl exec -i postgres-location-0 -- bash -c "psql -U $LOCATION_CT_DB_USERNAME -d $LOCATION_CT_DB_NAME"

cat ./db/udaconnect_public_location.sql | kubectl exec -i postgres-location-0 -- bash -c "psql -U $LOCATION_CT_DB_USERNAME -d $LOCATION_CT_DB_NAME"


# Cration locaiton kafka topic
`kubectl exec -i kafka-0 -n kafka-kraft -- bash -c "kafka-topics.sh --create --topic location --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092"`
