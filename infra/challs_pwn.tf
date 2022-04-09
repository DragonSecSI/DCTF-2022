module "chall_pwn_print" {
  source = "./modules/challs/pwn/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name = "print"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13370

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/printf:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_where_is_my_flag" {
  source = "./modules/challs/pwn/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name = "where-is-my-flag"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13371

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/where-is-my-flag:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_try_harder" {
  source = "./modules/challs/pwn/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name = "try-harder"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13372

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/try-harder:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_codechainz" {
  source = "./modules/challs/pwn/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name = "codechainz"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13373

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/codechainz:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_correct_horse_battery_staple" {
  source = "./modules/challs/pwn/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name = "correct-horse-battery-staple"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13374

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/correct-horse-battery-staple:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_padawan" {
  source = "./modules/challs/pwn/"
  count = var.dctfsi_challs_enabled ? 1 : 0

  name = "padawan"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13375

  k8s_namespace       = "default"
  k8s_image           = "dctfsi.azurecr.io/challs/padawan:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}
