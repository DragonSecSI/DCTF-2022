module "dctf_chall_webdb_sqltutor" {
  source = "./modules/challs/gcp/web_mysql/"

  name     = "sqltutor"
  hostname = "sqltutor.dragonsec.si"
  tls      = kubernetes_secret.tls_gcp.metadata.0.name
  initdb   = "${file("config/sqltutor_initdb.sql")}"

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/sqltutor:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  cloudflare_name    = "sqltutor"
  cloudflare_zone_id = data.cloudflare_zone.dragonsec.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1

  providers = {
    kubernetes.gcp = kubernetes
  }
}
