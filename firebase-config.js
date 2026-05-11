import { initializeApp } from "https://www.gstatic.com/firebasejs/12.6.0/firebase-app.js";

import {
  getAuth,
  onAuthStateChanged,
  signOut,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword
} from "https://www.gstatic.com/firebasejs/12.6.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyArjhwELyU01SqVJZONbrHGsSBkruLH6Rs",
  authDomain: "majkar-46764.firebaseapp.com",
  projectId: "majkar-46764",
  storageBucket: "majkar-46764.firebasestorage.app",
  messagingSenderId: "890907651693",
  appId: "1:890907651693:web:e21017d060571621aa9964"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export {
  auth,
  onAuthStateChanged,
  signOut,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword
};