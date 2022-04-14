resource "cloudflare_record" "dns" {
  zone_id = var.cloudflare_zone_id
  name    = var.cloudflare_name
  proxied = var.cloudflare_proxied
  value   = kubernetes_ingress.ingress.status.0.load_balancer.0.ingress.0.ip
  type    = "A"
  ttl     = var.cloudflare_ttl
}
