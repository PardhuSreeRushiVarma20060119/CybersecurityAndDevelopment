# 🔍 GraphQL Introspection & Injection

## ☠️ Why It's Dangerous

If introspection is **enabled in production**, attackers can:
- Discover all available queries, mutations, and types
- Identify sensitive endpoints (`passwordReset`, `userEmail`, `adminPanel`)
- Begin crafting injection attacks using discovered input parameters

---

## 🧪 Common Attacks

### 1. Introspection Enabled
- Use tools like:
  - `GraphQL Voyager`
  - `Altair` or `Insomnia`
  - `Postman`
- Send: `introspection.query`

### 2. GraphQL Injection (example)
```graphql
query {
  user(id: "1' OR '1'='1") {
    name
    email
  }
}
```
### 🔐 Defense
Disable introspection in production:
// Example in Apollo Server
introspection: process.env.NODE_ENV !== 'production'
Apply strict input validation and schema rules

Enforce authentication on sensitive queries

### 📚 Tools
GraphQLmap
InQL
Postman + Burp Proxy
GraphQL Voyager (visual mapping)
---

### 🧪 Optional: Create a file for attack payloads

#### ✅ File: `attack-payloads.graphql`
```graphql
# Sample GraphQL attack queries (for offline testing)

# Bypass logic (classic OR 1=1 style)
query {
  user(id: "1' || '1'=='1") {
    name
    email
  }
}
```
### Field injection (if raw queries allowed)
query {
  __typename
}

# Nested type exploitation
query {
  user(id: "123") {
    posts {
      title
      comments {
        content
        author {
          email
        }
      }
    }
  }
}