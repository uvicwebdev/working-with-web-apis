<!-- $theme: gaia -->

# UVic Web Development and Design Club
### Welcome all! :tada:

---
# Working with (Web) APIs :hammer:
---

# APIs :bulb:
* An API is:
	* an **interface** -- a special one!
	* like a **contract** that allows two developers that have never met to collaborate.
	* a **platform** for devs to build on.
* They let you tap into existing functionality **programmatically**.

---

# APIs :bulb:
* APIs are fundamental building blocks in software.
	* They free us from building stuff from scratch :sweat:
* If you've *ever* programmed, you've used an API
	* e.g. in C, a `.h` file defines an API
	* e.g. in Java, an `interface` defines an API
	* e.g. in JavaScript, the `Document` API lets you manipulate the DOM tree
	* e.g. in Python, ... ahh, you get the point.

---

# APIs :bulb:
* APIs are a natural part of **modularization**, where we organize our code logically into components
    * Each module hides the implementation details and exposes an API for other modules to use
* APIs exist at many "levels of abstraction"
	*  OSs, apps, and web services all interact with each other through APIs

---

# Web APIs :bulb: :bulb: :bulb:
* APIs available over the network (commonly HTTP)
* Accessible from around the world!
<div style="text-align: right">
  <img style="padding: 30px; display: inline-block;" width=200 height=200 src="/Users/juan/SYNERGY.jpg" />
  <img style="padding: 30px; display: inline-block;" width=200 height=200 src="/Users/juan/SYNERGY.jpg" />
  <img style="padding: 30px; display: inline-block;" width=200 height=200 src="/Users/juan/SYNERGY.jpg" />
  <img style="padding: 30px; display: inline-block;" width=200 height=200 src="/Users/juan/SYNERGY.jpg" />
  <img style="padding: 30px; display: inline-block;" width=200 height=200 src="/Users/juan/SYNERGY.jpg" />
	<img style="padding: 30px; display: inline-block;" width=200 height=200 src="/Users/juan/SYNERGY.jpg" />
</div>

---

# Building Platforms :house::house::house:
* Check out [this blog post](https://plus.google.com/112678702228711889851/posts/eVeouesvaVX) from 2011.
	* written by Steve Yegge, a software engineer and blogger who worked at Amazon and Google
* *Main idea:* build APIs into your software projects to tap into the pool of devs **around the world**.
	* Your product/service is valuable not only for its own features, but also the features of all **potential projects built on top of it**.

---

# Spotify APIs :musical_note:
* Spotify has multiple [public APIs](https://developer.spotify.com/documentation/), but we'll be using:
	* [Web API](https://developer.spotify.com/documentation/web-api/) to retrieve music metadata.
	* [Widgets API](https://developer.spotify.com/documentation/widgets/) to embed a Spotify player.
* Also, their Web Playback SDK allows streaming music on the browser through a JS library
	* Intended for use with Spotify Premium accounts. More flexible than the widgets API.

---
# Spotify Web API :musical_note:
* Allows you to programmatically:
	* Get data about [artists](https://developer.spotify.com/console/artists/), [songs](https://developer.spotify.com/console/tracks/), etc
	* Get [recommendations](https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/)
	* Get a Spotify [player](https://developer.spotify.com/documentation/web-api/reference/player/)
	* Edit [playlists](https://developer.spotify.com/documentation/web-api/reference/playlists/)
	* ...and other stuff!

---

# Making Requests :phone:
We can access Web APIs from anywhere that we can make HTTP requests:
* e.g. on front-end (i.e. from the browser) with JavaScript
* e.g. on back-end (i.e. from the server) with many different langauges -- in our case, with Python.

---