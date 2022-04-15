terraform {
  required_providers {
    kubernetes = {
      configuration_aliases = [kubernetes.gcp]
    }
    cloudflare = {
      source = "cloudflare/cloudflare"
      version = "~> 3.0"
    }
  }
}
