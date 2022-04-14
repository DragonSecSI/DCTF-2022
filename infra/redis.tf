module "redis" {
  source = "./modules/redis"

  name          = "dctf"
  k8s_namespace = "default"
  k8s_image     = "redis:6-alpine"
}
