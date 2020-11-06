provider "aws" {
    region     = "us-east-1"
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key
}

module "iam" {
    source = "./modules/iam"
}

module "s3" {
    source = "./modules/s3"
}

module "eb" {
    source       = "./modules/eb"
    profile_name = module.iam.profile_name
    bucket_name  = module.s3.bucket_name
}