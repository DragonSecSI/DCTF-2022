module "acme_wildcard_certificate" {
  source = "./modules/acme"

  registration_email = var.certificate_registration_email
  common_name        = "*.dragonsec.si"

  cloudflare_email   = var.cloudflare_email
  cloudflare_api_key = var.cloudflare_api_key
}

module "acme_dctf_root_certificate" {
  source = "./modules/acme"

  registration_email = var.certificate_registration_email
  common_name        = "dctf.si"

  cloudflare_email   = var.cloudflare_email
  cloudflare_api_key = var.cloudflare_api_key
}

module "acme_dctf_wildcard_certificate" {
  source = "./modules/acme"

  registration_email = var.certificate_registration_email
  common_name        = "*.dctf.si"

  cloudflare_email   = var.cloudflare_email
  cloudflare_api_key = var.cloudflare_api_key
}
