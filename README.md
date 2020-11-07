# leagueAPI

## Requisitos
- Terraform
- Docker
- EB CLI

## Local
### Startando o ambiente local
docker build -t league_api . && docker run --publish 80:80 --detach --name league_api league_api:latest
### Parando o ambiente local
docker stop league_api && docker rm league_api

## AWS

### Setup do terraform
Criar o terraform.tfvars na raiz do dir terraform com o seguinte conteudo:

```
# AWS Settings
aws_access_key = "..."
aws_secret_key = "..."
```

### Rodando o terraform
```
terraform init
terraform apply
```

### Deploy com eb cli
```
eb init -i
eb deploy
```