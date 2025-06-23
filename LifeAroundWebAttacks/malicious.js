// malicious.js

// Simulated cache poisoning payload
console.log("[malicious.js] ⚠️ Executing poisoned script.");

// This function could override legitimate behaviors if cached improperly
window.evilPayload = function () {
  alert("⚠️ Malicious JS executed from cache!");
};

// Simulated silent action
document.body.style.background = "#220000";
document.title = "You've been poisoned (simulated)";

// Overwrite an element if found
const labHeader = document.querySelector("h1");
if (labHeader) {
  labHeader.innerHTML = "💀 Simulated Cache Attack";
  labHeader.style.color = "#ff3333";
}