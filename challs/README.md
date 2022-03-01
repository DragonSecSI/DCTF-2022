# Creating a challenge

## Quick start

Choose a template from the `templates` folder depending on your needs, copy it to this folder and update the relevant files. After you're done and you need a review from the Repository owners create a new branch with your changes and a pull request. Quick details of the process is decribed below.

| Template | Files to edit                 | Description |
|---------:|:------------------------------|:------------|
| `pwn`    | `app.c`                       | For `pwn` or `rev` challenges which need a TCP server ([details](#pwn)) |
| `rev`    | `app.c`                       | For `rev` challenges which only pack a binary file ([details](#rev)) |
| `crypto` | `challenge.yml`               | For `crypto` challenges which pack a couple of files ([details](#crypto)) |
| `web`    | `challenge.yml`, `Dockerfile` | For `web` challenges which only provide a web service without other components (i.e. mysql) ([details](#web)) |

> When choosing a template it is recomended to read the linked details, so you can see why we made certain decisions.

When creating a misc challenge you might be able to use an existing template. If not, create your own setup and we'll integrate it in to the infra, but notify us in advance!


## Template details

### PWN

The `pwn` template is meant for challenges which need a raw socket server to function. This are usually `pwn` challenges, some `rev` challenges and in other cases `misc` challenges. Since we need to protect the containers running the challenges we prepared the template that leaves the flexibility of the possbile exploits but protects our resources like the local network and the flag file. In the case where this template is not enough for your needs you can create your own, but try to keep the below notes in mind. If there are any other questions you might have you can contact us on the DragonSec discord (@DCTF Team lead).

* Port should be set to 1337, since we'll provide a reverse proxy before the containers.
* The user and group IDs will be set later in the container, so you don't need to do it before. But do set the correct permissions for "other" users if needed.
* Challange files should be in the root directory, since that one will be set to read only.
* The description's IP and port will be appended later on, so no need to write it in the `challenge.yml`.

### Rev

In case you need a raw socket server to host a challenge you should take a look at the [pwn](#pwn) template. This `rev` template is for challenges that can be solved with just the binary or similar (i.e. in connection with `crypto`).

### Crypto

The only change you need here is updating the `challenge.yml` with the correct files for solving the challenge. If the challenge is connected with having a server, take a look at [pwn](#pwn) or if you need a binary but no server you can take a look at [rev](#rev).

### Web

This template of a `web` challenge is for single instance websites which don't connect to other services (like `mysql`). Since the web apps are so different it is hard to create a single template for them all, but here are some notes that you should follow.

* The web service should listen on `0.0.0.0:80`, since we have an overlaying reverse proxy set up later on.
* If you have a flag file, you should put it in the root directory (i.e. `/flag.txt`), since the root is better protected by the infrastructure.
* You need to update the `challenge.yml` file to provide the files needed. The only uploaded file should be a zip, for easier download (we might provide a simplified solution to automatically do this later on).
* With `web` challenges it's easier to just push the whole folder, but be mindful of everything you might not want there. As an example, the template has a `gen.py` file that generates the flag, but it's not included in the built docker image.

If your use case is different in any case feel free to create a different setup but coordinate that with the DragonSec team on discord (@DCTF Team lead).
