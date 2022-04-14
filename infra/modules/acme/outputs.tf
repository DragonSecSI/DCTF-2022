output "private_key" {
  value = acme_certificate.certificate.private_key_pem
  sensitive = true
}

output "certificate" {
  value = "${acme_certificate.certificate.certificate_pem}${acme_certificate.certificate.issuer_pem}"
}
