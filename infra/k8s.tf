resource "kubernetes_pod_security_policy" "k8s_psp" {
  metadata {
    name = "k8s-psp"
  }
  spec {
    privileged                 = false
    allow_privilege_escalation = false

    volumes = [
      "*",
    ]

    run_as_user {
      rule = "RunAsAny"
    }

    se_linux {
      rule = "RunAsAny"
    }

    supplemental_groups {
      rule = "RunAsAny"
    }

    fs_group {
      rule = "RunAsAny"
    }

    read_only_root_filesystem = true
  }
}

resource "kubernetes_secret" "tls" {
  metadata {
    name = "tls"
  }

  data = {
    "tls.crt" = module.acme_wildcard_certificate.certificate
    "tls.key" = module.acme_wildcard_certificate.private_key
  }

  type = "kubernetes.io/tls"
}

resource "kubernetes_secret" "dctf-root" {
  metadata {
    name = "dctf-root"
  }

  data = {
    "tls.crt" = module.acme_dctf_root_certificate.certificate
    "tls.key" = module.acme_dctf_root_certificate.private_key
  }

  type = "kubernetes.io/tls"
}

resource "kubernetes_secret" "dctf-wildcard" {
  metadata {
    name = "dctf-wildcard"
  }

  data = {
    "tls.crt" = module.acme_dctf_wildcard_certificate.certificate
    "tls.key" = module.acme_dctf_wildcard_certificate.private_key
  }

  type = "kubernetes.io/tls"
}

resource "kubernetes_secret" "registry_secret" {
  metadata {
    name = "registry-secret"
    namespace = var.azure_k8s_namespace
  }

  data = {
    ".dockerconfigjson" = var.azure_k8s_registry_secret
  }

  type = "kubernetes.io/dockerconfigjson"
}
