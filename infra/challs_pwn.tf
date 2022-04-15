module "dctf_chall_pwn_codechainz" {
  source = "./modules/challs/gcp/pwn/"

  name = "codechainz"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13370

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/codechainz:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_key_recovery" {
  source = "./modules/challs/gcp/pwn_root/"

  name = "key-recovery"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13371

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/key-recovery:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_macdonalds_1" {
  source = "./modules/challs/gcp/pwn/"

  name = "macdonalds-1"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13372

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/macdonalds-1:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_macdonalds_2" {
  source = "./modules/challs/gcp/pwn/"

  name = "macdonalds-2"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13373

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/macdonalds-2:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_snailtime" {
  source = "./modules/challs/gcp/pwn_root/"

  name = "snailtime"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13374

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/snailtime:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_vmstation" {
  source = "./modules/challs/gcp/pwn/"

  name = "vmstation"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13375

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/vmstation:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_maze" {
  source = "./modules/challs/gcp/pwn/"

  name = "maze"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13376

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/maze:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_dragons_lair" {
  source = "./modules/challs/gcp/pwn_root/"

  name = "dragons-lair"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13377

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/dragons-lair:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_correcthorsebatterystaple" {
  source = "./modules/challs/gcp/pwn/"

  name = "correcthorsebatterystaple"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13378

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/correcthorsebatterystaple:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_safespace" {
  source = "./modules/challs/gcp/pwn_root/"

  name = "safespace"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13379

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/safespace:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_phonebook" {
  source = "./modules/challs/gcp/pwn/"

  name = "phonebook"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13380

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/phonebook:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_shitty_tpm" {
  source = "./modules/challs/gcp/pwn/"

  name = "shitty-tpm"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13381

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/shitty-tpm:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_secure_kernel" {
  source = "./modules/challs/gcp/pwn/"

  name = "secure-kernel"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13382

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/secure-kernel:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}

module "dctf_chall_pwn_algebraic" {
  source = "./modules/challs/gcp/pwn_root/"

  name = "algebraic"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13383

  k8s_namespace       = "default"
  k8s_image           = "dctfint.azurecr.io/challs/algebraic:latest"
  k8s_registry_secret = kubernetes_secret.dctf_registry_secret.metadata.0.name

  providers = {
    kubernetes.gcp = kubernetes
  }
}
