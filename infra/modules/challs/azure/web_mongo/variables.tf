variable "name" {
  description = "Challenge name"
  type = string
  nullable = false
}

variable "hostname" {
  description = "Ingress hostname"
  type = string
  nullable = false
}

variable "tls" {
  description = "Ingress HTTPS tls"
  type = string
  nullable = false
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

variable "k8s_registry_secret" {
  description = "Kubernetes "
  type = string
  nullable = false
  sensitive = true
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
