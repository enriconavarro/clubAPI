output "db_endpoint" {
    value = aws_db_instance.instance.address
}

output "db_user" {
    value = aws_db_instance.instance.username
}

output "db_port" {
    value = aws_db_instance.instance.port
}

output "db_name" {
    value = aws_db_instance.instance.name
}