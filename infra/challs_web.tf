module "chall_web_eulers_license" {
  source = "./modules/challs/web/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name     = "eulers-license"
  hostname = "euler.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/eulers-license:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "euler"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1
}

module "chall_web_path" {
  source = "./modules/challs/web/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name     = "path"
  hostname = "path.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/path:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "path"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1
}

module "chall_web_rockjwt" {
  source = "./modules/challs/web/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name     = "rockjwt"
  hostname = "rockjwt.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/rockjwt:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "rockjwt"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1
}

module "chall_web_lolcode" {
  source = "./modules/challs/web/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name     = "lolcode"
  hostname = "lolcode.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/lolcode:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "lolcode"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1
}
