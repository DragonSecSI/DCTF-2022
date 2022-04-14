resource "tls_private_key" "private_key" {
  algorithm = "RSA"
}

resource "acme_registration" "registration" {
  account_key_pem = "${tls_private_key.private_key.private_key_pem}"
  email_address   = var.registration_email
}

resource "acme_certificate" "certificate" {
  account_key_pem           = "${acme_registration.registration.account_key_pem}"
  common_name               = var.common_name
  subject_alternative_names = var.alternative_names

  dns_challenge {
    provider = "cloudflare"
    config   = {
      CF_API_EMAIL = var.cloudflare_email
      CF_API_KEY   = var.cloudflare_api_key
    }
  }
}
