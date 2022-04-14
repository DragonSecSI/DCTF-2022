resource "kubernetes_service" "mongo_service" {
  metadata {
    name = "web-${var.name}-mongo-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.mongo_deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 27017
      target_port = 27017
    }

    type = "ClusterIP"
  }
}

resource "kubernetes_deployment" "mongo_deployment" {
  metadata {
    name = "web-${var.name}-mongo-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "${var.name}-mongo"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "${var.name}-mongo"
      }
    }

    template {
      metadata {
        labels = {
          app = "${var.name}-mongo"
        }
      }

      spec {
        container {
          image = "mongo:latest"
          name  = "${var.name}-mongo"

          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "0.2"
              memory = "128Mi"
            }
          }
        }
      }
    }
  }
}
