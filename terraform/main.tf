module "yandex-cloud" {
    source = "./modules/yandex"
    ssh_keys = var.ssh_keys
}

module "docker" {
    source = "./modules/docker"
}

module "github" {
    source = "./modules/github"
}

