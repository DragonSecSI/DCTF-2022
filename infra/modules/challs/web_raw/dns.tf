resource "cloudflare_record" "dns" {
  zone_id = var.cloudflare_zone_id
  name    = var.cloudflare_name
  proxied = var.cloudflare_proxied
  value   = var.ip
  type    = "A"
  ttl     = var.cloudflare_ttl
}
