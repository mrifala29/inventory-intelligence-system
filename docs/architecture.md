# Arsitektur Store Inventory Intelligence

## Komponen Utama
- Backend FastAPI
- WhatsApp Bot (AI Agent)
- Supabase (Database)
- AWS S3 (Storage)
- Frontend Next.js (minggu selanjutnya)

## Alur Singkat
1. Admin input produk → Backend → Simpan ke Supabase
2. Upload gambar → Backend → Upload ke S3
3. Bot WA → Query ke Backend → Kirim jawaban ke user