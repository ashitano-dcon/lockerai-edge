# Locker.ai Edge

Locker.ai Edge is a repository for edge devices to control the opening and closing of lockers.

## Setup locally 🖥️

If you want to build an environment more quickly without Docker, you can follow these steps to build your environment locally.

### Attention

- You need to install [rye](https://rye.astral.sh/guide/installation) before.

### 1. clone git repository

```bash
git clone "https://github.com/ashitano-dcon/lockerai-edge" && cd "./lockerai-edge"
```

### 2. set environment variables

See [`.env.example`](./.env.example) or contact the [repository owner](https://github.com/dino3616) for more details.

### 3. pin python version

```bash
rye pin $(cat "./.python-version")
```

### 4. install dependencies

```bash
rye sync
```

### 5. activate virtual environment

```bash
source "./.venv/bin/activate"
```

### 6. run script

```bash
rye run python -m main
```
