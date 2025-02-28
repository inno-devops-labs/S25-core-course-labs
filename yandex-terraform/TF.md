# Yandex Cloud Infrastracture Using Terraform

1. Firstly, the account on Yandex Cloud was created, this step was not complicated

2. I managed to found free-tier options but for some reasons my card was not attaching, thus I could not select VM

3. After that, I entirely followed Yandex Guide and it included:
- Get the authentication credentials
- Create a Terraform configuration file
- Configure a provider
- Prepare an infrastructure plan - I skipped this test because there was an error with subscription
- Create users- I skipped this test because there was an error with subscription
- Check and format configuration files- I skipped this test because there was an error with subscription

I used all the commands and configurations provided by Yandex, created all the needed files, for instance AppData\Roaming\terraform.rc

```bash
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

Configuration file was main.tf.

The main challenge was the guide itself since it is not quick at all, it has so unclear and inconsistent structure, also you have to go to many other pages just to follow the guide and all of them are very similar and not well-structured. Additionally, there was a problem with VPN, so I spend almost 2 hours trying to understand why even simple command like "terraform init" did not work and manage this situation by searching for working and free VPN, which is almost impossible.