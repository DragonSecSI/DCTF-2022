resource "kubernetes_service" "mysql_service" {
  metadata {
    name = "web-${var.name}-mysql-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.mysql_deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 3306
      target_port = 3306
    }

    type = "ClusterIP"
  }

  provider = kubernetes.gcp
}

resource "kubernetes_deployment" "mysql_deployment" {
  metadata {
    name = "web-${var.name}-mysql-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "${var.name}-mysql"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "${var.name}-mysql"
      }
    }

    template {
      metadata {
        labels = {
          app = "${var.name}-mysql"
        }
      }

      spec {
        container {
          image = "mysql:latest"
          name  = "${var.name}-mysql"

          env {
            name  = "MYSQL_RANDOM_ROOT_PASSWORD"
            value = "yes"
          }
          env {
            name  = "MYSQL_DATABASE"
            value = "database"
          }
          env {
            name  = "MYSQL_USER"
            value = "branko"
          }
          env {
            name  = "MYSQL_PASSWORD"
            value = "22b319a4880b353aa9659be58660241f9"
          }

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

          volume_mount {
            name = "initdb-volume"
            mount_path = "/docker-entrypoint-initdb.d/initdb.sql"
            sub_path = "initdb.sql"
          }
        }

        volume {
          name = "initdb-volume"
          config_map {
            name = kubernetes_config_map.initdb_configmap.metadata.0.name
            items {
              key = "initdb.sql"
              path = "initdb.sql"
            }
          }
        }
      }
    }
  }

  provider = kubernetes.gcp
}

resource "kubernetes_config_map" "initdb_configmap" {
  metadata {
    name = "web-${var.name}-configmap"
    namespace = var.k8s_namespace
  }

  data = {
    "initdb.sql" = var.initdb
  }

  provider = kubernetes.gcp
}
