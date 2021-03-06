resource "kubernetes_service" "service" {
  metadata {
    name = "pwn-${var.name}-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = var.port
      target_port = 1337
    }

    type = "LoadBalancer"
    load_balancer_ip = var.ip
  }

  provider = kubernetes.gcp
}

resource "kubernetes_deployment" "deployment" {
  metadata {
    name = "pwn-${var.name}-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "${var.name}"
    }
  }

  spec {
    replicas = var.replicas

    selector {
      match_labels = {
        app = "${var.name}"
      }
    }

    template {
      metadata {
        labels = {
          app = "${var.name}"
        }
      }

      spec {
        container {
          image = "${var.k8s_image}"
          name  = "${var.name}"

          #security_context {
          #  run_as_user     = 1337
          #  run_as_group    = 1337
          #  run_as_non_root = true
          #  capabilities {
          #    add = [
          #      "NET_BIND_SERVICE",
          #    ]
          #  }
          #}

          resources {
            limits = {
              cpu    = "1"
              memory = "1Gi"
            }
            requests = {
              cpu    = "0.5"
              memory = "1Gi"
            }
          }
        }

        image_pull_secrets {
          name = var.k8s_registry_secret
        }
      }
    }
  }

  provider = kubernetes.gcp
}
