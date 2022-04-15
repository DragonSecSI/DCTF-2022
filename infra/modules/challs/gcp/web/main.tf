resource "kubernetes_ingress" "ingress" {
  metadata {
    name = "web-${var.name}-ingress"
    namespace = var.k8s_namespace

    annotations = {
      "kubernetes.io/ingress.class" = "nginx"
    }
  }

  spec {
    rule {
      host = "${var.hostname}"
      http {
        path {
          backend {
            service_name = kubernetes_service.service.metadata.0.name
            service_port = 8000
          }

          path = "/"
        }
      }
    }

    tls {
      secret_name = var.tls
    }
  }

  wait_for_load_balancer = true

  provider = kubernetes.gcp
}

resource "kubernetes_service" "service" {
  metadata {
    name = "web-${var.name}-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 8000
      target_port = 8000
    }

    type = "ClusterIP"
  }

  provider = kubernetes.gcp
}

resource "kubernetes_deployment" "deployment" {
  metadata {
    name = "web-${var.name}-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "${var.name}"
    }
  }

  spec {
    replicas = 1

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

          env {
            name  = "SERVER_PORT"
            value = "8000"
          }
          env {
            name  = "SALT"
            value = "oeeeeooo"
          }
          env {
            name  = "NOT_FOUND"
            value = "dctf{L0g_4_hid3n_d@7@_n0t_s0_h@rd_righ7}"
          }
          env {
            name  = "WEB_COOKIE"
            value = "sup3rs3cr3tC00ki3"
          }

          resources {
            limits = {
              cpu    = "0.3"
              memory = "512Mi"
            }
            requests = {
              cpu    = "0.1"
              memory = "128Mi"
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
