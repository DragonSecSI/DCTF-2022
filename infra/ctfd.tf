#module "ctfdsi" {
#  source = "./modules/ctfd"
#
#  name     = "ctfdsi"
#  revision = 1
#
#  k8s_namespace  = "default"
#  k8s_image      = "ajuvan/ctfd:latest"
#  k8s_hostname   = "dctf.si"
#  k8s_secret_tls = kubernetes_secret.dctf-root.metadata.0.name
#
#  azure_resource_group_name     = "MC_${azurerm_resource_group.challs.name}_${azurerm_kubernetes_cluster.k8s.name}_${azurerm_resource_group.challs.location}"
#  azure_resource_group_location = azurerm_resource_group.challs.location
#
#  cloudflare_name    = "@"
#  cloudflare_zone_id = data.cloudflare_zone.dctf.id
#  cloudflare_proxied = false
#  cloudflare_ttl     = 1
#
#  config_secret_key   = var.dctfsi_config_secret_key
#  config_database_url = "postgresql+psycopg2://${var.dctfsi_postgres_user}:${var.dctfsi_postgres_password}@${module.postgresql.service_name}:5432/${var.dctfsi_postgres_database}"
#  config_redis_url    = "redis://${module.redis.service_name}:6379/1"
#
#  config_mail_from_addr        = var.dctfsi_config_mail_from_addr
#  config_mail_sender_addr      = var.dctfsi_config_mail_sender_addr
#  config_mail_server           = var.dctfsi_config_mail_server
#  config_mail_port             = var.dctfsi_config_mail_port
#  config_mail_auth_enabled     = var.dctfsi_config_mail_auth_enabled
#  config_mail_auth_username    = var.dctfsi_config_mail_auth_username
#  config_mail_auth_password    = var.dctfsi_config_mail_auth_password
#  config_mail_auth_tls_enabled = var.dctfsi_config_mail_auth_tls_enabled
#  config_mail_auth_ssl_enabled = var.dctfsi_config_mail_auth_ssl_enabled
#}

#module "ctfd" {
#  source = "./modules/ctfd"
#
#  name     = "ctfd"
#  revision = 0
#
#  k8s_namespace  = "default"
#  k8s_image      = "ajuvan/ctfd:latest"
#  k8s_hostname   = "dctf.dragonsec.si"
#  k8s_secret_tls = kubernetes_secret.tls.metadata.0.name
#
#  azure_resource_group_name     = "MC_${azurerm_resource_group.challs.name}_${azurerm_kubernetes_cluster.k8s.name}_${azurerm_resource_group.challs.location}"
#  azure_resource_group_location = azurerm_resource_group.challs.location
#
#  cloudflare_name    = "dctf"
#  cloudflare_zone_id = data.cloudflare_zone.dragonsec.id
#  cloudflare_proxied = true
#  cloudflare_ttl     = 1
#
#  config_secret_key   = var.dctf_config_secret_key
#  config_database_url = "postgresql+psycopg2://${var.dctf_postgres_user}:${var.dctf_postgres_password}@${module.postgresql-international.service_name}:5432/${var.dctf_postgres_database}"
#  config_redis_url    = "redis://${module.redis.service_name}:6379/2"
#
#  config_mail_from_addr        = var.dctf_config_mail_from_addr
#  config_mail_sender_addr      = var.dctf_config_mail_sender_addr
#  config_mail_server           = var.dctf_config_mail_server
#  config_mail_port             = var.dctf_config_mail_port
#  config_mail_auth_enabled     = var.dctf_config_mail_auth_enabled
#  config_mail_auth_username    = var.dctf_config_mail_auth_username
#  config_mail_auth_password    = var.dctf_config_mail_auth_password
#  config_mail_auth_tls_enabled = var.dctf_config_mail_auth_tls_enabled
#  config_mail_auth_ssl_enabled = var.dctf_config_mail_auth_ssl_enabled
#}
