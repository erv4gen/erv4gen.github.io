# Use the official Jekyll dev container image as a base
# This image includes Ruby, Bundler, Jekyll, Node.js, and other common tools.
# See https://github.com/devcontainers/images/tree/main/src/jekyll
# Trying a more general tag or a different well-known one, as :0-3 was not found.
# Let's try the image name that often defaults to a stable version.
FROM mcr.microsoft.com/vscode/devcontainers/jekyll

# Switch to root to install system packages
USER root

# Install Python and pip
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Symlink python3 to python so python scripts run, use -f to force overwrite if symlink exists
RUN ln -sf /usr/bin/python3 /usr/bin/python \
    && ln -sf /usr/bin/pip3 /usr/bin/pip

# Switch back to the non-root vscode user
USER vscode

# Copy Gemfile and Gemfile.lock (if it exists)
# Copying Gemfile.lock ensures consistent gem versions if it's present.
WORKDIR /tmp
COPY Gemfile Gemfile.lock* ./ 
# The '*' after Gemfile.lock handles the case where it might not exist yet.

# Install gems specified in Gemfile
# This will also create/update Gemfile.lock in the container's /tmp directory.
# We'll copy it back to the workspace later if needed, or rely on VS Code to sync.
RUN bundle install

# The WORKDIR is typically set by the dev container extension to /workspaces/your-project-name
# So, explicitly setting WORKDIR /workspaces/${localWorkspaceFolderBasename} might be redundant or problematic
# if $localWorkspaceFolderBasename is not correctly interpolated by this specific build stage.
# We'll rely on the default behavior.

# Optional: If you have Python requirements, uncomment and add:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# This Dockerfile sets up Ruby (from base image), Jekyll (via bundle install),
# and Python. When the dev container starts, VS Code will typically mount
# your project directory into /workspaces/${localWorkspaceFolderBasename}.
