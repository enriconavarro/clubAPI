provider "aws" {
    region     = "us-east-1"
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key
}

variable "db_pass" {
  type = string
}

module "iam" {
    source = "./modules/iam"
}

module "s3" {
    source = "./modules/s3"
}

module "rds" {
    source  = "./modules/rds"
    db_pass = var.db_pass
}

module "eb" {
    source       = "./modules/eb"
    profile_name = module.iam.profile_name
    bucket_name  = module.s3.bucket_name
    db_endpoint  = module.rds.db_endpoint
    db_user      = module.rds.db_user
    db_port      = module.rds.db_port
    db_name      = module.rds.db_name
    db_password  = var.db_pass
}