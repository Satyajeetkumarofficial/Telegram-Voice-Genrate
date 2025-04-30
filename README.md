# Telegram Voice Bot (Text-to-Speech Bot)

Yeh Telegram bot Hindi, Hinglish aur English text ko **voice** me convert karta hai aur aapko **audio message** ke roop me bhejta hai. Saath hi `/txt` se **.txt file**, `/start` pe welcome greeting aur `/broadcast` se admin users sabko message bhej sakte hain.

## Commands:

- `/start`  
  User ko greet karega ("Good Morning", "Good Afternoon", "Good Night") unke naam ke saath.

- `/bol <text>`  
  Hindi me voice message generate karta hai.

- `/speak <text>`  
  English me voice message generate karta hai.

- `/txt <text>`  
  Diya gaya text ek `.txt` file me save karke bhejta hai.

- `/broadcast <message>`  
  (Sirf admin ke liye) – Sab users ko ek message broadcast karta hai.

## How to Deploy on Koyeb or Any Server

1. `.env` file create karein aur is format me fill karein:
