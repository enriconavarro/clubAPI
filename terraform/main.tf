provider "aws" {
    region     = "us-east-1"
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key
}

module "iam" {
    source = "./modules/iam"
}

module "eb" {
    source       = "./modules/eb"
    profile_name = module.iam.profile_name
}