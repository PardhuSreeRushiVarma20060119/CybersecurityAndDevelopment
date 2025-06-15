// pollution-demo.js
let payload = JSON.parse('{"__proto__":{"isAdmin":true}}');

// Imagine this happens in the app:
let user = {};
console.log(user.isAdmin); // true, polluted globally

// Use in environments like Node.js or client JS apps where this leads to privilege escalation or logic bypass.