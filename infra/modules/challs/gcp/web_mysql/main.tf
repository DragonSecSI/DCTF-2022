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

          security_context {
            run_as_user     = 1337
            run_as_group    = 1337
            run_as_non_root = true
            capabilities {
              add = [
                "NET_BIND_SERVICE",
              ]
            }
          }

          env {
            name = "SQLTUT_PORT"
            value = "8000"
          }
          env {
            name = "SQLTUT_HOST"
            value = "0.0.0.0"
          }
          env {
            name = "SQLTUT_DBURI"
            value = "mysql://branko:22b319a4880b353aa9659be58660241f9@${kubernetes_service.mysql_service.metadata.0.name}/database"
          }
          env {
            name = "SQLTUT_HASHING_SECRET"
            value = "v3s01jc7"
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
