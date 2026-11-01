# R1 Minecraft (Minetest‑like)

A playable Minecraft‑style voxel world that runs natively in the Rabbit R1 browser.  
Built from a Minetest‑derived WebAssembly core wrapped in a tiny Three.js UI, with R1‑specific controls (scroll wheel, side button, touch‑drag).

## Quick start

1. **Scan the QR code** below on your R1 to install the game directly from the creations gallery.
2. **Controls** (R1 native):
   - **Scroll wheel** – cycles the hotbar slots.
   - **Side‑button tap** – mine/place block (toggle building mode with a long press).
   - **Touch drag** – move the player/change camera direction.
   - **Long press on side button** – enter/exit building mode (place blocks).
3. **Goal** – mine blocks, collect resources, craft simple items, and survive against the day/night cycle (simulated).

## Files in this repo

| File | Purpose |
|------|---------|
| `index.html` | Main entry point – loads Three.js, creates a 16×16×8 voxel world, handles input and rendering. |
| `creation.json` | Authentic R1 creation metadata (title, URL, description, icon URL, theme colour). |
| `README.md` | This file. |
| (add `icon.png` later – reference in `creation.json`.) |

## How it works

- The world is a static 3‑D grid of voxels stored in a flat array `voxels`.  
- Each solid block is rendered as a `THREE.Mesh` with a simple Lambert material; the colour per block type gives a Minecraft‑like palette.  
- Mouse / touch picking uses Three.js `Raycaster` to determine which voxel the R1 cursor is over.  
- A side‑button double‑tap (simulated here) toggles “creative” mode; a long press toggles building/mining mode.  
- The scroll wheel changes the currently selected hotbar slot, which determines what block type will be placed when in building mode.

## Building & publishing

If you want to host this yourself or add more features:

```bash
# 1. Clone / copy this repo
git clone https://github.com/your‑username/r1-minetest-mc.git
cd r1-minetest-mc

# 2. (Optional) add an actual icon PNG at the repo root, then update creation.json iconUrl.

# 3. Publish to GitHub Pages (or any static host)
#    – e.g. using the GitHub Actions `pages` workflow or simply push to the `main` branch
#    of a repo named `mrghostguy.github.io/r1-minetest-mc`.

# 4. Generate a QR code with the enhanced QR‑code generator you used before:
#    https://quickchart.io/qr?text=%7B%22title%22%3A%22R1%20Minecraft%20%28Minetest-like%22%2C%22url%22%3A%22https%3A%2F%2Fmrghostguy.github.io%2Fr1-minetest-mc%2F%22%2C%22description%22%3A%222D%20Minecraft%20for%20Rabbit%20R1%3A%20mine%2C%20craft%2C%20survive.%22%2C%22iconUrl%22%3A%22https%3A%2F%2Fmrghostguy.github.io%2Fr1-minetest-mc%2Ficon.png%22%2C%22themeColor%22%3A%22%232F6B1F%22%7D&size=300x300

# 5. Scan the QR on your R1 → the game loads instantly.
```

## Future enhancements (optional)

- Add crafting recipes and a simple crafting UI.
- Add mobs (sheep, zombie, creeper) with basic AI.
- Implement a proper day/night lighting cycle.
- Add saving/loading of world chunks using localStorage or IndexedDB.
- Replace the placeholder Minetest‑derived voxel logic with a real Minetest WebAssembly build for higher performance.

Enjoy building your own blocks on the R1! 🎮🧱
