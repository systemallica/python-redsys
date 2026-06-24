# Create a new version
# ------------------------------------------------------------------------------
version-patch:
	uv run semantic-release version --patch

version-minor:
	uv run semantic-release version --minor

version-major:
	uv run semantic-release version --major
