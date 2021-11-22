#!/bin/bash
set -e

echo "START Running Vuejs on `date`"
export NODE_OPTIONS=--openssl-legacy-provider
cd frontend
npm run serve