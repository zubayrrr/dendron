---
id: 84nah5q9kfvfoku1r0qqis3
title: Spotify   Code Snippet
desc: ''
updated: 1652786937487
created: 1652786937487
tags:
  - articles
---

# [Spotify - Code Snippet](https://leerob.io/snippets/spotify-top-tracks)

```
import { getTopTracks } from '../../lib/spotify';

export default async (_, res) => {
  const response = await getTopTracks();
  const { items } = await response.json();

  const tracks = items.slice(0, 10).map((track) => ({
    artist: track.artists.map((_artist) => _artist.name).join(', '),
    songUrl: track.external_urls.spotify,
    title: track.name
  }));

  return res.status(200).json({ tracks });
};
```

```
// lib/spotify.js

import fetch from 'isomorphic-unfetch';
import querystring from 'querystring';

const client_id = process.env.SPOTIFY_CLIENT_ID;
const client_secret = process.env.SPOTIFY_CLIENT_SECRET;
const refresh_token = process.env.SPOTIFY_REFRESH_TOKEN;

const basic = Buffer.from(`${client_id}:${client_secret}`).toString('base64');
const TOP_TRACKS_ENDPOINT = `https://api.spotify.com/v1/me/top/tracks`;
const TOKEN_ENDPOINT = `https://accounts.spotify.com/api/token`;

const getAccessToken = async () => {
  const response = await fetch(TOKEN_ENDPOINT, {
    method: 'POST',
    headers: {
      Authorization: `Basic ${basic}`,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: querystring.stringify({
      grant_type: 'refresh_token',
      refresh_token
    })
  });

  return response.json();
};

export const getTopTracks = async () => {
  const { access_token } = await getAccessToken();

  return fetch(TOP_TRACKS_ENDPOINT, {
    headers: {
      Authorization: `Bearer ${access_token}`
    }
  });
};
```

## [](https://leerob.io/#usage)Usage

1

### Create Spotify Application

First, we need to create a Spotify application to give us credentials to authenticate with the API.

-   Go to your [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
-   Click **Create an App**.
-   Fill out the name and description and click **create**.
-   Click **Show Client Secret**.
-   Save your Client ID and Secret. You'll need these soon.
-   Click **Edit Settings**.
-   Add `http://localhost:3000` as a redirect URI.

All done! You now have a properly configured Spotify application and the correct credentials to make requests.

2

### Authentication

There are a variety of ways to authenticate with the Spotify API, depending on your application. Since we only need permission granted *once*, we'll use the [Authorization Code Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow).

First, we'll have our application request authorization by logging in with whatever [scopes](https://developer.spotify.com/documentation/general/guides/authorization-guide/#list-of-scopes) we need. Here's an example of what the URL might look like. Swap out the `client_id` and scopes for your own.

```
https://accounts.spotify.com/authorize?client_id=8e94bde7dd
b84a1f7a0e51bf3bc95be8&response_type=code&redirect_uri=http
%3A%2F%2Flocalhost:3000&scope=user-read-currently-playing%20
user-top-read
```

After authorizing, you'll be redirected back to your `redirect_uri`. In the URL, there's a `code` query parameter. Save this value.

```
http://localhost:3000/callback?code=NApCCg..BkWtQ
```

Next, we'll need to retrieve the refresh token. You'll need to generate a Base 64 encoded string containing the client ID and secret from earlier. You can use [this tool](https://www.base64encode.org/) to encode it online. The format should be `client_id:client_secret`.

```
curl -H "Authorization: Basic <base64 encoded client_id:client_secret>"
-d grant_type=authorization_code -d code=<code> -d redirect_uri=http%3A
%2F%2Flocalhost:3000 https://accounts.spotify.com/api/token
```

This will return a JSON response containing a `refresh_token`. This token is [valid indefinitely](https://github.com/spotify/web-api/issues/374) unless you revoke access, so we'll want to save this in an environment variable.

3

### Add Environment Variables

To securely access the API, we need to include the secret with each request. We also *do not* want to commit secrets to git. Thus, we should use an environment variable. Learn how to add [environment variables in Vercel](https://vercel.com/docs/environment-variables).
