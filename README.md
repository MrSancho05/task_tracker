# Task Tracker CLI (Python)

## Loyihaning maqsadi
Task Tracker — bu terminal (komanda qatori) orqali boshqariladigan vazifalar (tasklar) ro‘yxatini yaratish, ko‘rish va saqlash imkonini beruvchi kichik Python CLI dasturidir. Vazifalar JSON formatida faylda saqlanadi va istalgan vaqtda o‘qilishi mumkin.

---

## Hozirgi holat (Progress)

- `tasks.json` faylini o‘qish va yozish uchun `load_tasks()` va `save_tasks()` funksiyalari yozildi.
- `load_tasks()` funksiyasi fayl mavjud bo‘lmasa bo‘sh ro‘yxat qaytaradi.
- `save_tasks()` funksiyasi Pythondagi ro‘yxatni JSON faylga chiroyli formatda yozadi.
- `main.py` faylida vazifalarni yuklab olish, yangi task qo‘shish va ularni faylga saqlash jarayoni bajarilmoqda.
- Vazifa har doim quyidagi maydonlarga ega:
  - `id` — yagona raqamli identifikator
  - `description` — vazifa matni
  - `status` — vazifa holati (masalan, `todo`)
  - `createdAt` va `updatedAt` — ISO 8601 formatidagi sanalar va vaqtlar

---

## Loyihaning keyingi qadamlari

- Terminaldan kiruvchi komandalar (`add`, `list`, `update`, `delete`, `mark-in-progress`, `mark-done`) funksiyalarini yaratish
- Xatoliklarni tutish va foydalanuvchiga ma’lumot berish
- Kodingizni modullarga ajratish va tozalash

---

## Loyihani ishga tushirish

1. `main.py` va `tasks.py` fayllari bir papkada joylashgan bo‘lishi kerak.
2. Terminalda papkaga o‘ting va quyidagilarni bajarib ko‘ring:

```bash
python main.py
