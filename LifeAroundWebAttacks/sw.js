// sw.js
self.addEventListener('install', event => {
  console.log('🔧 Service Worker installed (simulated malicious behavior)');
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  console.log('🔥 Service Worker activated');
});

self.addEventListener('fetch', event => {
  if (event.request.url.includes('sensitive-data')) {
    event.respondWith(
      new Response('<h1>Intercepted!</h1>', {
        headers: { 'Content-Type': 'text/html' }
      })
    );
  } else {
    event.respondWith(fetch(event.request));
  }
});
