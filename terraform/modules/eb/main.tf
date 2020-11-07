resource "aws_elastic_beanstalk_application" "app" {
  name        = "league-api"
  description = "Elastic beanstalk criado para o league_api"
}

resource "aws_elastic_beanstalk_environment" "env" {
  name                = "league-api"
  application         = aws_elastic_beanstalk_application.app.name
  solution_stack_name = "64bit Amazon Linux 2 v3.2.0 running Docker"

  setting {
    namespace = "aws:ec2:instances"
    name      = "InstanceTypes"
    value     = "t2.micro"
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = var.profile_name
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "bucket_name"
    value     = var.bucket_name
  }
}