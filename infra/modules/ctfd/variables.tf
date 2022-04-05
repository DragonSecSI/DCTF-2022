variable "name" {
  description = "Module instance name"
  type = string
  nullable = false
}

variable "revision" {
  description = "Revision to force redeploy"
  type = number
  default = 0
}

variable "k8s_namespace" {
  description = "Kubernetes namespace"
  type = string
  default = "default"
}

variable "k8s_image" {
  description = "Kubernetes container image"
  type = string
  nullable = false
}

variable "k8s_hostname" {
  description = "Kubernetes ingress hostname"
  type = string
  nullable = false
}

variable "k8s_secret_tls" {
  description = "Kubernetes secret for TLS certificates"
  type = string
  nullable = false
}

variable "cloudflare_zone_id" {
  description = "Cloudflare zone id"
  type = string
  nullable = false
}

variable "cloudflare_name" {
  description = "Cloudflare entry name without domain"
  type = string
  nullable = false
}

variable "cloudflare_proxied" {
  description = "Cloudflare proxied status"
  type = bool
  nullable = false
}

variable "cloudflare_ttl" {
  description = "Cloudflare proxied status"
  type = number
  default = 3600
}

variable "config_secret_key" {
  description = "Secret key for token signing"
  type = string
  nullable = false
  sensitive = true
}

variable "config_database_url" {
  description = "Database connection url"
  type = string
  nullable = false
  sensitive = true
}

variable "config_redis_url" {
  description = "Redis connection url"
  type = string
  sensitive = true
}

variable "config_mail_from_addr" {
  description = "Email address to send from"
  type = string
}

variable "config_mail_sender_addr" {
  description = "Email responsible for sending the email"
  type = string
}

variable "config_mail_server" {
  description = "Email server"
  type = string
}

variable "config_mail_port" {
  description = "Email server port"
  type = string
}

variable "config_mail_auth_enabled" {
  description = "Use authentication when sending"
  type = bool
}

variable "config_mail_auth_username" {
  description = "Username used for authentication"
  type = string
}

variable "config_mail_auth_password" {
  description = "Password used for authentication"
  type = string
  sensitive = true
}

variable "config_mail_auth_tls_enabled" {
  description = "Use TLS to connect"
  type = bool
}

variable "config_mail_auth_ssl_enabled" {
  description = "Use SSL to connect"
  type = bool
}
