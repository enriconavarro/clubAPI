# clubAPI

## Run in dev environment
docker build -t club_api . && docker run --publish 8000:8000 --detach --name club_api club_api:latest

### Stop in dev environment
docker stop club_api && docker rm club_api