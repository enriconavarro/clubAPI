resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}

resource "aws_security_group" "postgres_port_sg" {
  name        = "postgres_port_sg"
  description = "Allow traffic in 5432"
  vpc_id      = aws_default_vpc.default.id

  ingress {
    description = "Postgres port rule"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    # Only for dev ;)
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "instance" {
  vpc_security_group_ids = [aws_security_group.postgres_port_sg.id]
  allocated_storage      = 20
  storage_type           = "gp2"
  engine                 = "postgres"
  engine_version         = "12.4"
  instance_class         = "db.t2.micro"
  name                   = "league_db"
  username               = "league_db_user"
  password               = var.db_pass
  port                   = 5432
}