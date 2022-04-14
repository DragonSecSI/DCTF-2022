module "chall_webdb_web_course" {
  source = "./modules/challs/web_mongo/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name     = "web-course"
  hostname = "web-course.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/web-course:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "web-course"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1
}
