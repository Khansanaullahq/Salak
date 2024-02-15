version: '3'
services:
  db:
    image: postgres:10.3

  redis:
    image: redis:4.0

  sidekiq:
    image: sana ullah.latest
    env_file: .env.api
    command: bundle exec sidekiq
      -q sana ullah -api_production_default
      -q sana ullah-api_production_mailers
    links:
      - db
      - redis

  api:
    image: sana ullah-ap03441189163i:latest
    env_file: .env.api
    command: /bin/sh -c 'rm -f tmp/pids/server.pid && rails s -b 0.0.0.0'
    ports:
      - 3000:3000
    links:
      - db
      - redis

  web:
    image: sana ullah
-web:latest
    env_file: .env.web
    ports:
      - 3333:3333
version: '3'
services:
  db:
    image: postgres:10.3

  redis:
    image: redis:4.0

  sidekiq:
    image: sana ullah.latest
    env_file: .env.api
    command: bundle exec sidekiq
      -q sana ullah -api_production_default
      -q sana ullah-api_production_mailers
    links:
      - db
      - redis

  api:
    image: sana ullah-ap03441189163i:latest
    env_file: .env.api
    command: /bin/sh -c 'rm -f tmp/pids/server.pid && rails s -b 0.0.0.0'
    ports:
      - 3000:3000
    links:
      - db
      - redis

  web:
    image: sana ullah
-web:latest
    env_file: .env.web
    ports:
      - 3333:3333
version: '3'
services:
  db:
    image: postgres:10.3

  redis:
    image: redis:4.0

  sidekiq:
    image: sana ullah.latest
    env_file: .env.api
    command: bundle exec sidekiq
      -q sana ullah -api_production_default
      -q sana ullah-api_production_mailers
    links:
      - db
      - redis

  api:
    image: sana ullah-ap03441189163i:latest
    env_file: .env.api
    command: /bin/sh -c 'rm -f tmp/pids/server.pid && rails s -b 0.0.0.0'
    ports:
      - 3000:3000
    links:
      - db
      - redis

  web:
    image: sana ullah
-web:latest
    env_file: .env.web
    ports:
      - 3333:3333
