## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| aws | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| bucket\_name | Nome do bucket para armazenar o backup do banco da aplicacao. | `string` | n/a | yes |
| db\_endpoint | Endpoint para conexao com o db. | `string` | n/a | yes |
| db\_name | Nome do db. | `string` | n/a | yes |
| db\_password | Password para acesso ao db. | `string` | n/a | yes |
| db\_port | Porta para conexao com o db. | `number` | n/a | yes |
| db\_user | Username para acesso ao db. | `string` | n/a | yes |
| profile\_name | Nome da role para as maquinas do EB assumirem. | `string` | n/a | yes |

## Outputs

No output.

