variable "name" {
  description = "Module instance name"
  type = string
  nullable = false
}

variable "azure_resource_group_name" {
  description = "Azure target resource group name"
  type = string
  nullable = false
}

variable "azure_resource_group_location" {
  description = "Azure target resource group location"
  type = string
  nullable = false
}

variable "azure_disk_type" {
  description = "Azure managed disk type"
  type = string
  nullable = false
}

variable "azure_disk_size" {
  description = "Azure managed disk size"
  type = string
  nullable = false
}

variable "postgres_user" {
  description = "Postgres initial user"
  type = string
  nullable = false
}

variable "postgres_password" {
  description = "Postgres initial password"
  type = string
  nullable = false
  sensitive = true
}

variable "postgres_database" {
  description = "Postgres initial database"
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
