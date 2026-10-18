# Build stage
ARG CADDY_VERSION=2.11.7
FROM caddy:${CADDY_VERSION}-builder AS builder

# Build Caddy with the Cloudflare DNS module
# Newly added:
# Rate limit module, and ipfilter-caddy
# These work and are currently in use for my main website.
RUN xcaddy build \
    --with github.com/caddy-dns/cloudflare \
    --with github.com/WeidiDeng/caddy-cloudflare-ip \
    --with github.com/fvbommel/caddy-combine-ip-ranges \
	--with github.com/mholt/caddy-ratelimit \
    --with github.com/jpillora/ipfilter-caddy

# Final stage
FROM caddy:${CADDY_VERSION}

# Copy the custom-built Caddy binary
COPY --from=builder /usr/bin/caddy /usr/bin/caddy
