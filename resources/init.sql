CREATE TYPE license_type AS ENUM ('perpetual', 'timed', 'trial');

CREATE TABLE IF NOT EXISTS license(
    license_key VARCHAR(20) PRIMARY KEY,
    product TEXT,
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    expiration TIMESTAMPTZ,
    type license_type NOT NULL,
    description TEXT
);