module "dctf_chall_web_eulers_license" {
  source = "./modules/challs/gcp/web/"

  name     = "eulers-license"
  hostname = "euler.dragonsec.si"
  tls      = kubernetes_secret.tls_gcp.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/eulers-license:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  cloudflare_name    = "euler"
  cloudflare_zone_id = data.cloudflare_zone.dragonsec.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_web_book_store" {
  source = "./modules/challs/gcp/web/"

  name     = "book-store"
  hostname = "book-store.dragonsec.si"
  tls      = kubernetes_secret.tls_gcp.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/book-store:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  cloudflare_name    = "book-store"
  cloudflare_zone_id = data.cloudflare_zone.dragonsec.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1

  providers = {
    kubernetes.gcp = kubernetes
  }
}
