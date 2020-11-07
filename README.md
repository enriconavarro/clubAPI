# leagueAPI

## Requisitos
- Terraform
- Docker
- Docker-compose
- EB CLI

## Local
### Startando o ambiente local
cd local/
docker-compose up --build -d
### Parando o ambiente local
docker-compose down

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