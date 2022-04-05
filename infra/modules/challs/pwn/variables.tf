variable "name" {
  description = "Challenge name"
  type = string
  nullable = false
}

variable "ip" {
  description = "Challenge public IP"
  type = string
  nullable = false
}

variable "port" {
  description = "Challenge public port"
  type = number
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
