docker build -t oyelowo/udaconnect-frontend ./modules/frontend
docker push oyelowo/udaconnect-frontend

docker build -t oyelowo/udaconnect-location ./modules/location
docker push oyelowo/udaconnect-location

docker build -t oyelowo/udaconnect-api ./modules/api
docker push oyelowo/udaconnect-api

docker build -t oyelowo/udaconnect-person ./modules/person
docker push oyelowo/udaconnect-person
