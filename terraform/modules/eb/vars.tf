variable "profile_name" {
  type = string
  description = "Nome da role para as maquinas do EB assumirem."
}

variable "bucket_name" {
  type = string
  description = "Nome do bucket para armazenar o backup do banco da aplicacao."
}