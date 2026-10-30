# ootBot
Discord Bot for the Ocarina of Time Speedrunning Server

## Running with Docker
- Copy `config-template.yml` to `config.yml` and fill it in.
- Start the bot: `docker compose up -d`
- Stop the bot: `docker compose down`
- View logs: `docker compose logs --follow`
- After changing dependencies in `requirements.txt`, rebuild with `docker compose build`.

The repository is mounted into the container, so `config.yml` lives in this directory. If `auto_update` is set to `True`, the bot pulls updates itself and exits, and Docker restarts it on the new code (replacing `run-loop.sh`).

## Updating a server
`./deploy.sh user@host [remote_dir]` connects to the server over SSH, clones or pulls the bot into `remote_dir` (default `ootBot`), then rebuilds and restarts the container. Add `--config` to also upload your local `config.yml`, e.g. on the first deploy: `./deploy.sh --config root@your-droplet-ip`.
