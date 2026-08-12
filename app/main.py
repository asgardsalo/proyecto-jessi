from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Del campo a tu oficina")

# Mount static folder so photos can be served
static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def read_root():
    photo_dir = static_dir / "photos"
    photos = []
    if photo_dir.exists():
        photos = [f"/static/photos/{p.name}" for p in sorted(photo_dir.iterdir()) if p.is_file()]

    photo_cards = "".join(
        f"<div style='margin: 12px; text-align:center;'><img src='{src}' alt='photo' style='max-width:220px; max-height:220px; border-radius:12px;'/></div>"
        for src in photos
    )

    return f"""
    <html>
        <head>
            <title>Del campo a tu oficina</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f8f2; color: #1f3a2f; }}
                .hero {{ padding: 40px; text-align: center; background: #ffffff; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
                .cards {{ display: flex; flex-wrap: wrap; justify-content: center; padding: 24px; gap: 12px; }}
                .hero h1 {{ margin: 0 0 12px; }}
                .hero p {{ margin: 0; font-size: 1.05rem; color: #4a5a48; }}
            </style>
        </head>
        <body>
            <div class="hero">
                <h1>Del campo a tu oficina</h1>
                <p>Un espacio para ver productos frescos y fotos del campo listos para tu oficina.</p>
            </div>
            <div class="cards">{photo_cards}</div>
        </body>
    </html>
    """
