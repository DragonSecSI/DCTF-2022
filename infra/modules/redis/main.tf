resource "kubernetes_service" "service" {
  metadata {
    name = "redis-${var.name}-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 6379
      target_port = 6379
    }

    type = "ClusterIP"
  }
}

resource "kubernetes_deployment" "deployment" {
  metadata {
    name = "redis-${var.name}-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "redis-${var.name}"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "redis-${var.name}"
      }
    }

    template {
      metadata {
        labels = {
          app = "redis-${var.name}"
        }
      }

      spec {
        container {
          image = "${var.k8s_image}"
          name  = "redis-${var.name}"

          resources {
            limits = {
              cpu    = "1"
              memory = "4Gi"
            }
            requests = {
              cpu    = "0.2"
              memory = "512Mi"
            }
          }
        }
      }
    }
  }
}
