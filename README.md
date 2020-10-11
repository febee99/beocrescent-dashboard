# Beo Crescent Dashboard

This dashboard was built with Nuxt.js (Vue) on the frontend and Python Flask on the backend. Currently, the dashboard is live on:

**Frontend** 

```
http://d2b9ybaeuz42aa.cloudfront.net/
```

**Backend** 

```
https://ui2lc3zrbc.execute-api.ap-southeast-1.amazonaws.com/dev
```

> Contact Emmanuel (Telegram: @theodorayy) for deploying changes on the frontend, and Kelvin (Telegram: @kelvinngsl) for deploying changes on the backend.

## Frontend Setup

Change your directory to `/dashboard` and run the following:

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

## Backend Setup

Change your directory to `/api` and run the following:

**For macOS**

```bash
# install dependencies for the first time
$ sh install.sh

# Run the Flask app
$ sh run.sh
```