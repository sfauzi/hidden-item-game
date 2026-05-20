# 🎯 Hidden Item Game

Program command-line sederhana berbasis Python untuk permainan menemukan item tersembunyi di dalam grid. Pemain bernavigasi dari posisi awal mengikuti urutan langkah tertentu (Utara → Timur → Selatan) untuk menemukan kemungkinan lokasi item yang tersembunyi.

---

## 📁 Struktur File

```
hidden_item_game.py   ← File utama program
README.md             ← Dokumentasi ini
```

---

## 🗺️ Layout Grid

Program menggunakan grid berukuran **6 baris × 8 kolom** dengan layout berikut:

```
########
#......#
#.##...#
#...#.##
#X#....#
########
```

### Legenda Simbol

| Simbol | Arti |
|--------|------|
| `#` | Rintangan / obstacle — tidak bisa dilewati |
| `.` | Jalur bebas / clear path — bisa dilewati |
| `X` | Posisi awal pemain |
| `$` | Kemungkinan lokasi item (ditampilkan setelah kalkulasi) |

> Posisi awal `X` berada di **row 4, col 1** (indeks dimulai dari 0, pojok kiri atas).

---

## ⚙️ Cara Kerja Program

### Alur Navigasi

Dari posisi awal `X`, pemain bergerak dalam **urutan tetap**:

```
1. Ke atas  (Up/North)  → A langkah
2. Ke kanan (Right/East) → B langkah
3. Ke bawah (Down/South) → C langkah
```

Setiap sel yang dilewati **wajib berupa jalur bebas** (`.` atau `X`). Jika ada rintangan (`#`) yang menghalangi di tengah perjalanan, rute tersebut dianggap tidak valid dan tidak menghasilkan lokasi item.

### Contoh Navigasi

Dengan input **Up=3, Right=4, Down=2**:

```
Langkah 1 — Naik 3 sel:
  (4,1) → (3,1) → (2,1) → (1,1)  ✓ semua jalur bebas

Langkah 2 — Kanan 4 sel:
  (1,1) → (1,2) → (1,3) → (1,4) → (1,5)  ✓ semua jalur bebas

Langkah 3 — Turun 2 sel:
  (1,5) → (2,5) → (3,5)  ✓ mendarat di jalur bebas

Hasil: Item kemungkinan ada di (row=3, col=5)
```

Grid dengan marker `$`:
```
########
#......#
#.##...#
#...#$##   ← $ di (3,5)
#X#....#
########
```

---

## 🚀 Cara Menjalankan

### Prasyarat

- Python **3.6** atau lebih baru
- Tidak memerlukan library tambahan (hanya built-in Python)

### Menjalankan Program

```bash
python3 hidden_item_game.py
```

### Input yang Dibutuhkan

Program akan meminta 3 input secara berurutan:

```
Steps UP    (A): <jumlah langkah ke atas>
Steps RIGHT (B): <jumlah langkah ke kanan>
Steps DOWN  (C): <jumlah langkah ke bawah>
```

> Tekan **Enter** tanpa mengetik angka untuk menggunakan nilai default: **Up=3, Right=4, Down=2**

---

## 📋 Contoh Output Lengkap

```
=============================================
        *** HIDDEN ITEM GAME ***
=============================================

[GRID LAYOUT]

  ########
  #......#
  #.##...#
  #...#.##
  #X#....#
  ########

  Player 'X' starts at → row 4, col 1  (0-indexed)

[NAVIGATION INPUT]
  Enter number of steps for each direction.
  (Press Enter to use example: Up=3, Right=4, Down=2)

  Steps UP    (A): 3
  Steps RIGHT (B): 4
  Steps DOWN  (C): 2

  Route: Up 3 → Right 4 → Down 2

=============================================
  PROBABLE ITEM LOCATION(S)
=============================================
  → (row=3, col=5)

[GRID WITH PROBABLE LOCATIONS MARKED AS '$']

  ########
  #......#
  #.##...#
  #...#$##
  #X#....#
  ########

=============================================
  Good luck finding the hidden item! 🎯
=============================================
```

---

## 🔍 Penjelasan Fungsi

### `find_player(grid)`
Mencari posisi awal pemain (`X`) di dalam grid secara otomatis. Mengembalikan koordinat `(row, col)`.

### `is_walkable(grid, r, c)`
Mengecek apakah suatu sel dapat dilewati — yaitu berada di dalam batas grid dan bukan rintangan (`#`).

### `navigate(grid, start_r, start_c, steps_up, steps_right, steps_down)`
Fungsi utama kalkulasi. Mensimulasikan perjalanan 3 fase (Atas → Kanan → Bawah) dan mengembalikan **set koordinat** dari semua posisi akhir yang valid dan berada di jalur bebas.

### `display_grid(grid, highlights=None)`
Menampilkan grid ke terminal. Jika parameter `highlights` diisi dengan sekumpulan koordinat, sel-sel tersebut ditampilkan dengan simbol `$`.

### `main()`
Fungsi pengendali utama: menampilkan grid, membaca input pengguna, menjalankan navigasi, dan mencetak hasil beserta grid bonus.

---

## ⚠️ Penanganan Error

| Kondisi | Penanganan |
|---------|------------|
| Input bukan angka | Program menampilkan peringatan dan menggunakan nilai default |
| Input kosong (Enter) | Menggunakan nilai default (Up=3, Right=4, Down=2) |
| Jalur terhalang rintangan | Rute tidak valid, tidak menghasilkan lokasi |
| Tidak ada lokasi yang ditemukan | Menampilkan pesan "No reachable clear-path cell found" |

---

## 🧩 Sistem Koordinat

Program menggunakan sistem koordinat **baris-kolom (row, col)** berbasis 0:

```
        col: 0  1  2  3  4  5  6  7
   row 0 → [ #  #  #  #  #  #  #  # ]
   row 1 → [ #  .  .  .  .  .  .  # ]
   row 2 → [ #  .  #  #  .  .  .  # ]
   row 3 → [ #  .  .  .  #  .  #  # ]
   row 4 → [ #  X  #  .  .  .  .  # ]
   row 5 → [ #  #  #  #  #  #  #  # ]
```

- Bergerak **ke atas** → nilai `row` berkurang
- Bergerak **ke bawah** → nilai `row` bertambah
- Bergerak **ke kanan** → nilai `col` bertambah
- Bergerak **ke kiri** → nilai `col` berkurang

---

## 💡 Tips Menemukan Item

Gunakan tabel ini sebagai panduan memilih nilai A, B, C yang menghasilkan lokasi valid:

| Up (A) | Right (B) | Down (C) | Lokasi Item |
|--------|-----------|----------|-------------|
| 3 | 4 | 2 | (row=3, col=5) ✅ |
| 1 | 2 | 0 | (row=3, col=3) ✅ |
| 2 | 0 | 1 | (row=3, col=1) ✅ |
| 2 | 3 | 1 | ✗ Terhalang obstacle |

---

*Dibuat dengan Python 3 — Tidak memerlukan instalasi library tambahan.*
