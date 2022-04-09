# Secrets

cloudflare_email   = ""
cloudflare_api_key = ""

azure_client_id       = ""
azure_client_secret   = ""
azure_tenant_id       = ""
azure_subscription_id = ""


# Configuration

azure_resource_group_name     = "DCTF2022-Challs"
azure_resource_group_location = "West Europe"

azure_k8s_vm_type         = "standard_d2as_v5"
azure_k8s_auto_scaling    = false
azure_k8s_nodes_count     = 1
azure_k8s_nodes_min_count = null
azure_k8s_nodes_max_count = null

azure_k8s_registry_secret = ""
azure_k8s_pwn_namespace   = "default"

certificate_registration_email = "andraz.juvan@dragonsec.si"


# DCTF SI configuration

dctfsi_postgres_name = "dctfsi"
dctfsi_challs_enabled = false

dctfsi_postgres_user     = "dctf"
dctfsi_postgres_password = ""
dctfsi_postgres_database = "dctf"

dctfsi_postgres_azure_disk_type = "StandardSSD_LRS"
dctfsi_postgres_azure_disk_size = "100"

dctfsi_config_secret_key = ""
dctfsi_config_mail_from_addr = ""
dctfsi_config_mail_sender_addr = ""
dctfsi_config_mail_server = ""
dctfsi_config_mail_port = 25
dctfsi_config_mail_auth_enabled = false
dctfsi_config_mail_auth_username = ""
dctfsi_config_mail_auth_password = ""
dctfsi_config_mail_auth_tls_enabled = false
dctfsi_config_mail_auth_ssl_enabled = false


# DCTF Int configuration

dctf_postgres_name = "dctf"

dctf_postgres_user     = "dctf"
dctf_postgres_password = ""
dctf_postgres_database = "dctf"

dctf_postgres_azure_disk_type = "StandardSSD_LRS"
dctf_postgres_azure_disk_size = "100"

dctf_config_secret_key = ""
dctf_config_mail_from_addr = ""
dctf_config_mail_sender_addr = ""
dctf_config_mail_server = ""
dctf_config_mail_port = 25
dctf_config_mail_auth_enabled = false
dctf_config_mail_auth_username = ""
dctf_config_mail_auth_password = ""
dctf_config_mail_auth_tls_enabled = false
dctf_config_mail_auth_ssl_enabled = false
