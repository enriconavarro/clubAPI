# clubAPI

## Local
### Startando o ambiente local
docker build -t club_api . && docker run --publish 8000:8000 --detach --name club_api club_api:latest
### Parando o ambiente local
docker stop club_api && docker rm club_api

## AWS

### Setup do terraform
Criar o terraform.tfvars na raiz do dir terraform com o seguinte conteudo:
\# AWS Settings
aws_access_key = "..."
aws_secret_key = "..."

### Rodando o terraform
terraform init
terraform apply