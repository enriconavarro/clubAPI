variable "profile_name" {
  type = string
  description = "Nome da role para as maquinas do EB assumirem."
}

variable "bucket_name" {
  type = string
  description = "Nome do bucket para armazenar o backup do banco da aplicacao."
}

variable "db_endpoint" {
  type = string
  description = "Endpoint para conexao com o db."
}

variable "db_user" {
  type = string
  description = "Username para acesso ao db."
}

variable "db_password" {
  type = string
  description = "Password para acesso ao db."
}

variable "db_port" {
  type = number
  description = "Porta para conexao com o db."
}

variable "db_name" {
  type = string
  description = "Nome do db."
}