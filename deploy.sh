#!/bin/bash
# Updates the bot on a server (e.g. a DigitalOcean droplet) running it with Docker.
# Pulls the latest code, rebuilds the image so dependency changes are picked up, and restarts the container.
#
# Usage: ./deploy.sh [--config] user@host [remote_dir]
#   --config     also upload the local config.yml to the server
#   remote_dir   where the bot lives on the server (default: ootBot, relative to the user's home)

set -euo pipefail

repo_url='https://github.com/fig02/ootBot.git'

upload_config=n
if [ "${1:-}" = '--config' ]; then
	upload_config=y
	shift
fi

if [ $# -lt 1 ]; then
	echo "Usage: $0 [--config] user@host [remote_dir]"
	exit 1
fi

host=$1
remote_dir=${2:-ootBot}

# clone on first deploy, otherwise pull the latest code
ssh "$host" bash -s -- "$repo_url" "$remote_dir" <<'EOF'
set -euo pipefail
if [ ! -d "$2/.git" ]; then
	git clone "$1" "$2"
else
	git -C "$2" pull --ff-only
fi
EOF

if [ "$upload_config" = y ]; then
	scp "$(dirname "$0")/config.yml" "$host:$remote_dir/config.yml"
	ssh "$host" chmod 600 "$remote_dir/config.yml"
fi

# rebuild and restart the container, then clear out the old image
ssh "$host" bash -s -- "$remote_dir" <<'EOF'
set -euo pipefail
cd "$1"
if [ ! -f config.yml ]; then
	echo "config.yml is missing on the server. Rerun with --config to upload yours."
	exit 1
fi
docker compose up -d --build
docker image prune -f
docker compose ps
sleep 5
docker compose logs --tail 20
EOF
