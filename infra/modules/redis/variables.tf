variable "name" {
  description = "Instance name"
  type = string
  nullable = false
}

variable "k8s_namespace" {
  description = "Instance name"
  type = string
  default = "default"
}

variable "k8s_image" {
  description = "Instance name"
  type = string
  nullable = false
}

