resource "aws_s3_bucket" "bucket" {
  bucket = "backup-bucket-${uuid()}"
  acl    = "private"
}