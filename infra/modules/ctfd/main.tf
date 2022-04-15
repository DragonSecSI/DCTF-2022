resource "kubernetes_ingress" "ingress" {
  metadata {
    name = "ctfd-${var.name}-ingress"
    namespace = var.k8s_namespace

    annotations = {
      "kubernetes.io/ingress.class" = "nginx"
    }
  }

  spec {
    rule {
      host = "${var.k8s_hostname}"
      http {
        path {
          backend {
            service_name = kubernetes_service.service.metadata.0.name
            service_port = 80
          }

          path = "/"
        }
      }
    }

    tls {
      secret_name = var.k8s_secret_tls
    }
  }

  wait_for_load_balancer = true
}

resource "kubernetes_service" "service" {
  metadata {
    name = "ctfd-${var.name}-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 80
      target_port = 8000
    }

    type = "ClusterIP"
  }
}

resource "kubernetes_deployment" "deployment" {
  metadata {
    name = "ctfd-${var.name}-deployment"
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
          revision = "${var.revision}"
        }
      }

      spec {
        container {
          image = "${var.k8s_image}"
          name  = "${var.name}"

          env {
            name = "SECRET_KEY"
            value = "${var.config_secret_key}"
          }
          env {
            name = "DATABASE_URL"
            value = "${var.config_database_url}"
          }
          env {
            name = "REDIS_URL"
            value = "${var.config_redis_url}"
          }
          env {
            name = "MAILFROM_ADDR"
            value = "${var.config_mail_from_addr}"
          }
          env {
            name = "MAILSENDER_ADDR"
            value = "${var.config_mail_sender_addr}"
          }
          env {
            name = "MAIL_SERVER"
            value = "${var.config_mail_server}"
          }
          env {
            name = "MAIL_PORT"
            value = "${var.config_mail_port}"
          }
          env {
            name = "MAIL_USEAUTH"
            value = "${var.config_mail_auth_enabled}"
          }
          env {
            name = "MAIL_USERNAME"
            value = "${var.config_mail_auth_username}"
          }
          env {
            name = "MAIL_PASSWORD"
            value = "${var.config_mail_auth_password}"
          }
          env {
            name = "MAIL_TLS"
            value = "${var.config_mail_auth_tls_enabled}"
          }
          env {
            name = "MAIL_SSL"
            value = "${var.config_mail_auth_ssl_enabled}"
          }

          resources {
            limits = {
              cpu    = "2"
              memory = "4Gi"
            }
            requests = {
              cpu    = "1.5"
              memory = "3Gi"
            }
          }
        }
      }
    }
  }
}
