variable "registration_email" {
  description = "Let's encrypt registration email"
  type = string
  nullable = false
}

variable "common_name" {
  description = "Certificate common name"
  type = string
  nullable = false
}

variable "alternative_names" {
  description = "Additional certificate alternative names"
  type = list
  default = []
}

variable cloudflare_email {
  description = "Cloudflare email"
  type = string
  nullable = false
}

variable cloudflare_api_key {
  description = "Cloudflare API key"
  type = string
  sensitive = true
  nullable = false
}
