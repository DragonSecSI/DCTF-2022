# Cloudflare

variable "cloudflare_email" {
  description = "Cloudflare email"
  type        = string
  nullable    = false
}

variable "cloudflare_api_key" {
  description = "Cloudflare API key"
  type        = string
  sensitive   = true
  nullable    = false
}

# Azure

variable "azure_client_id" {
  description = "Azure service principal client ID"
  type        = string
  nullable    = false
}

variable "azure_client_secret" {
  description = "Azure service principal client secret"
  type        = string
  sensitive   = true
  nullable    = false
}

variable "azure_tenant_id" {
  description = "Azure service principal tenant"
  type        = string
  nullable    = false
}

variable "azure_subscription_id" {
  description = "Azure subscription_id"
  type        = string
  nullable    = false
}

# Config

variable "azure_resource_group_name" {}
variable "azure_resource_group_location" {}

variable "azure_k8s_vm_type" {}
variable "azure_k8s_auto_scaling" {}
variable "azure_k8s_nodes_count" {}
variable "azure_k8s_nodes_min_count" {}
variable "azure_k8s_nodes_max_count" {}

variable "azure_k8s_registry_secret" {}
variable "azure_k8s_pwn_namespace" {}

variable "certificate_registration_email" {}

variable "dctfsi_postgres_name" {}
variable "dctfsi_postgres_user" {}
variable "dctfsi_postgres_password" {}
variable "dctfsi_postgres_database" {}
variable "dctfsi_postgres_azure_disk_type" {}
variable "dctfsi_postgres_azure_disk_size" {}
variable "dctfsi_config_secret_key" {}
variable "dctfsi_config_mail_from_addr" {}
variable "dctfsi_config_mail_sender_addr" {}
variable "dctfsi_config_mail_server" {}
variable "dctfsi_config_mail_port" {}
variable "dctfsi_config_mail_auth_enabled" {}
variable "dctfsi_config_mail_auth_username" {}
variable "dctfsi_config_mail_auth_password" {}
variable "dctfsi_config_mail_auth_tls_enabled" {}
variable "dctfsi_config_mail_auth_ssl_enabled" {}

variable "dctf_postgres_name" {}
variable "dctf_postgres_user" {}
variable "dctf_postgres_password" {}
variable "dctf_postgres_database" {}
variable "dctf_postgres_azure_disk_type" {}
variable "dctf_postgres_azure_disk_size" {}
variable "dctf_config_secret_key" {}
variable "dctf_config_mail_from_addr" {}
variable "dctf_config_mail_sender_addr" {}
variable "dctf_config_mail_server" {}
variable "dctf_config_mail_port" {}
variable "dctf_config_mail_auth_enabled" {}
variable "dctf_config_mail_auth_username" {}
variable "dctf_config_mail_auth_password" {}
variable "dctf_config_mail_auth_tls_enabled" {}
variable "dctf_config_mail_auth_ssl_enabled" {}
