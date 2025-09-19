self.addEventListener("install", (event) => {
  console.log("Service Worker: Installed");
  event.waitUntil(
    caches.open("bus-tracker-cache").then((cache) => {
      return cache.addAll([
        "./index.html",
        "./manifest.json",
        "https://unpkg.com/leaflet/dist/leaflet.css",
        "https://unpkg.com/leaflet/dist/leaflet.js",
        "https://unpkg.com/leaflet-routing-machine/dist/leaflet-routing-machine.css",
        "https://unpkg.com/leaflet-routing-machine/dist/leaflet-routing-machine.js"
      ]);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
