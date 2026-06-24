# Create a new version
# ------------------------------------------------------------------------------
version-patch:
	uv run semantic-release publish --patch

version-minor:
	uv run semantic-release publish --minor

version-major:
	uv run semantic-release publish --major
